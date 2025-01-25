from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum, max, avg, when, current_timestamp,min
import os
from delta import configure_spark_with_delta_pip
os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}/bin:" + os.environ["PATH"]


# Initialize SparkSession with Delta Lake support
builder = SparkSession.builder \
    .appName("Lakehouse Gold Layer") \
    .master("local[1]") \
    .config("spark.sql.shuffle.partitions", "2") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Define input (silver) and output (gold) paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
silver_path = os.path.join(current_dir, "02-silver")
gold_path = os.path.join(current_dir, "03-gold")

# Ensure the output directory exists
os.makedirs(gold_path, exist_ok=True)

# Function to create customer segmentation table
def create_customer_segmentation_table(customers, accounts, transactions):
    # Join accounts and transactions
    accounts_transactions = accounts.join(
        transactions,
        accounts.account_id == transactions.account_id,
        "left"
    )

    # Aggregate customer insights
    customer_insights = accounts_transactions.groupBy("customer_id").agg(
        sum("balance").alias("total_balance"),
        count("transaction_id").alias("transaction_count"),
        avg("amount").alias("average_transaction_amount")
    )

    # Join with customers to create segmentation
    customer_segmentation = customers.join(
        customer_insights,
        customers.customer_id == customer_insights.customer_id,
        "left"
    ).select(
        customers.customer_id,
        customers.name.alias("full_name"),
        customers.email,
        when(col("total_balance") >= 50000, "Platinum")
        .when(col("total_balance") >= 20000, "Gold")
        .when(col("total_balance") >= 5000, "Silver")
        .otherwise("Basic").alias("segment"),
        "total_balance",
        "transaction_count",
        "average_transaction_amount",
        current_timestamp().alias("processed_at")
    )

    # Write to Delta (Gold Layer)
    customer_segmentation.write.format("delta").mode("overwrite").save(f"{gold_path}/customer_segmentation")
    print("Gold table created: Customer Segmentation")

# Function to create credit card analysis table
def create_credit_card_analysis_table(credit_cards, accounts, transactions):
    # Step 1: Join credit_cards with accounts using customer_id
    cards_with_accounts = credit_cards.join(
        accounts,
        credit_cards.customer_id == accounts.customer_id,
        "inner"
    )

    # Step 2: Join the resulting DataFrame with transactions using account_id
    card_transactions = cards_with_accounts.join(
        transactions,
        cards_with_accounts.account_id == transactions.account_id,
        "left"
    )

    # Debugging: Print schemas and sample data
    print("Schema of credit_cards:")
    credit_cards.printSchema()
    credit_cards.show(5)
    print("Schema of accounts:")
    accounts.printSchema()
    accounts.show(5)
    print("Schema of transactions:")
    transactions.printSchema()
    transactions.show(5)
    print("Joined card_transactions:")
    card_transactions.show(5)

    # Step 3: Aggregate credit card insights
    credit_card_analysis = card_transactions.groupBy("card_id").agg(
        avg("amount").alias("average_spending"),
        max("amount").alias("max_transaction"),
        sum("amount").alias("total_spending"),
        max("credit_limit").alias("credit_limit"),
        (sum("amount") / max("credit_limit")).alias("utilization_rate"),
        current_timestamp().alias("processed_at")
    )

    # Debugging: Show aggregated data
    print("Aggregated credit card analysis:")
    credit_card_analysis.show(5)

    # Step 4: Write to Delta (Gold Layer)
    credit_card_analysis.write.format("delta").mode("overwrite").save(f"{gold_path}/credit_card_analysis")
    print("Gold table created: Credit Card Analysis")

# Function to create fraud detection table
def create_fraud_detection_table(transactions, digital_activity):
    # Filter suspicious transactions
    suspicious_transactions = transactions.filter(
        (col("amount") > 10000) | (col("transaction_type") == "unusual")
    ).select(
        "transaction_id",
        "account_id",
        "amount",
        col("transaction_date").alias("transaction_timestamp"),
        current_timestamp().alias("processed_at")
    )

    # Identify multiple failed login attempts
    failed_logins = digital_activity.filter(col("activity_type") == "login_failed").groupBy(
        "customer_id"
    ).agg(
        min(col("timestamp")).alias("first_failed_login"),
        count("*").alias("failed_login_count")
    ).filter(
        col("failed_login_count") > 3
    )

    # Write suspicious transactions to Delta (Gold Layer)
    suspicious_transactions.write.format("delta").mode("overwrite").save(f"{gold_path}/suspicious_transactions")
    print("Gold table created: Suspicious Transactions")

    # Write failed login attempts to Delta (Gold Layer)
    failed_logins.write.format("delta").mode("overwrite").save(f"{gold_path}/failed_logins")
    print("Gold table created: Failed Logins")

# Load Silver tables
silver_customers = spark.read.format("delta").load(f"{silver_path}/customers")
silver_accounts = spark.read.format("delta").load(f"{silver_path}/accounts")
silver_transactions = spark.read.format("delta").load(f"{silver_path}/transactions")
silver_credit_cards = spark.read.format("delta").load(f"{silver_path}/credit_cards")
silver_digital_activity = spark.read.format("delta").load(f"{silver_path}/digital_activity")

# Generate Gold tables
create_customer_segmentation_table(silver_customers, silver_accounts, silver_transactions)
create_credit_card_analysis_table(silver_credit_cards, silver_accounts, silver_transactions)
create_fraud_detection_table(silver_transactions, silver_digital_activity)

print("Gold layer populated successfully.")
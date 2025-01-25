from pyspark.sql import SparkSession
import os
from delta import configure_spark_with_delta_pip
from pyspark.sql.functions import col, current_timestamp
os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}/bin:" + os.environ["PATH"]


# Initialize SparkSession with Delta Lake support
builder = SparkSession.builder \
    .appName("Lakehouse Silver Layer") \
    .master("local[1]") \
    .config("spark.sql.shuffle.partitions", "2") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Define input (bronze) and output (silver) paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
bronze_path = os.path.join(current_dir, "01-bronze")
silver_path = os.path.join(current_dir, "02-silver")

# Ensure the output directory exists
os.makedirs(silver_path, exist_ok=True)

# List of datasets
datasets = [
    "customers", "accounts", "transactions", "loans",
    "credit_cards", "branches", "compliance",
    "investments", "digital_activity"
]

# Transformation functions for Silver layer
def transform_customers(df):
    return df.select(
        col("customer_id"),
        col("name"),
        col("email"),
        col("phone_number"),
        col("address"),
        col("customer_type"),
        col("cpf"),
        col("cnpj"),
        col("created_at"),
        col("updated_at")
    ).filter(col("email").isNotNull())

def transform_accounts(df):
    return df.select(
        col("account_id"),
        col("customer_id"),
        col("account_type"),
        col("balance"),
        col("currency"),
        col("created_at"),
        col("updated_at")
    )

def transform_transactions(df):
    return df.select(
        col("transaction_id"),
        col("account_id"),
        col("transaction_type"),
        col("amount"),
        col("transaction_date"),
        col("description")
    ).filter(col("amount") > 0)

def transform_loans(df):
    return df.select(
        col("loan_id"),
        col("customer_id"),
        col("loan_type"),
        col("loan_amount"),
        col("interest_rate"),
        col("term"),
        col("start_date"),
        col("end_date"),
        col("loan_status")
    )

def transform_credit_cards(df):
    return df.select(
        col("card_id"),
        col("customer_id"),
        col("card_number"),
        col("card_type"),
        col("expiry_date"),
        col("credit_limit"),
        col("current_balance"),
        col("created_at"),
        col("updated_at"),
        current_timestamp().alias("processed_at")
    )

def transform_branches(df):
    return df.select(
        col("branch_id"),
        col("branch_name"),
        col("address"),
        col("phone_number"),
        col("created_at"),
        col("updated_at")
    )

def transform_compliance(df):
    return df.select(
        col("compliance_id"),
        col("customer_id"),
        col("compliance_type"),
        col("status"),
        col("review_date"),
        col("comments")
    )

def transform_investments(df):
    return df.select(
        col("investment_id"),
        col("customer_id"),
        col("investment_type"),
        col("amount"),
        col("purchase_date"),
        col("maturity_date")
    )

def transform_digital_activity(df):
    return df.select(
        col("activity_id"),
        col("customer_id"),
        col("activity_type"),
        col("timestamp")
    )

# Map dataset names to transformation functions
transformations = {
    "customers": transform_customers,
    "accounts": transform_accounts,
    "transactions": transform_transactions,
    "loans": transform_loans,
    "credit_cards": transform_credit_cards,
    "branches": transform_branches,
    "compliance": transform_compliance,
    "investments": transform_investments,
    "digital_activity": transform_digital_activity
}

# Process each dataset
for dataset in datasets:
    input_path = os.path.join(bronze_path, dataset)
    output_path = os.path.join(silver_path, dataset)

    # Check if input Delta table exists
    if not os.path.exists(input_path):
        print(f"Warning: Bronze table not found: {input_path}. Skipping...")
        continue

    # Read from Delta (Bronze Layer)
    try:
        df = spark.read.format("delta").load(input_path)
        print(f"Loaded Bronze table for {dataset}")

        # Apply transformation
        if dataset in transformations:
            df_transformed = transformations[dataset](df)
            df_transformed = df_transformed.withColumn("processed_at", current_timestamp())

            # Write to Delta (Silver Layer)
            df_transformed.write.format("delta").mode("overwrite").save(output_path)
            print(f"Silver table for {dataset} written to {output_path}")

        else:
            print(f"No transformation defined for {dataset}. Skipping...")

    except Exception as e:
        print(f"Error processing {dataset}: {e}")

print("Silver layer populated successfully.")
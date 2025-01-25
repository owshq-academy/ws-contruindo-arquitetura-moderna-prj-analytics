from pyspark.sql import SparkSession
import os
from delta import configure_spark_with_delta_pip

os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}/bin:" + os.environ["PATH"]

# Initialize SparkSession with Delta Lake support
builder = SparkSession.builder \
    .appName("Read Gold Delta Tables") \
    .master("local[1]") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Define the path to the gold Delta tables
current_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
gold_path = os.path.join(current_dir, "03-gold")

# List of Gold tables to read
gold_tables = [
    "customer_segmentation",
    "credit_card_analysis",
    "suspicious_transactions",
    "failed_logins"
]

# Read and display each table
for table in gold_tables:
    table_path = os.path.join(gold_path, table)

    # Check if the table exists
    if not os.path.exists(table_path):
        print(f"Warning: Gold table not found: {table_path}")
        continue

    # Read the table
    try:
        df = spark.read.format("delta").load(table_path)
        print(f"\nContents of Gold table: {table}")
        df.show(truncate=False)
    except Exception as e:
        print(f"Error reading Gold table {table}: {e}")

print("Finished reading Gold Delta tables.")
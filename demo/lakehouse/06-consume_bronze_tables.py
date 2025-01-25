from pyspark.sql import SparkSession
import os
from delta import configure_spark_with_delta_pip

os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}/bin:" + os.environ["PATH"]

# Initialize SparkSession with Delta Lake support
builder = SparkSession.builder \
    .appName("Read Bronze Tables") \
    .master("local[1]") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Define input path for Bronze tables
current_dir = os.path.dirname(os.path.abspath(__file__))
bronze_path = os.path.join(current_dir, "01-bronze")

# List of Bronze tables
bronze_tables = [
    "customers", "accounts", "transactions", "loans",
    "credit_cards", "branches", "compliance",
    "investments", "digital_activity"
]

# Read and display Bronze tables
for table in bronze_tables:
    path = os.path.join(bronze_path, table)
    if os.path.exists(path):
        print(f"\nContents of Bronze table: {table}")
        try:
            spark.read.format("delta").load(path).show(truncate=False)
        except Exception as e:
            print(f"Error reading Bronze table {table}: {e}")
    else:
        print(f"Bronze table {table} does not exist at path: {path}")

print("\nFinished reading Bronze tables.")
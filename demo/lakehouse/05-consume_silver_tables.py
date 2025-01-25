from pyspark.sql import SparkSession
import os
from delta import configure_spark_with_delta_pip

os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}/bin:" + os.environ["PATH"]

# Initialize SparkSession with Delta Lake support
builder = SparkSession.builder \
    .appName("Read Silver Tables") \
    .master("local[1]") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Define input path for Silver tables
current_dir = os.path.dirname(os.path.abspath(__file__))
silver_path = os.path.join(current_dir, "02-silver")

# List of Silver tables
silver_tables = [
    "customers", "accounts", "transactions", "loans",
    "credit_cards", "branches", "compliance",
    "investments", "digital_activity"
]

# Read and display Silver tables
for table in silver_tables:
    path = os.path.join(silver_path, table)
    if os.path.exists(path):
        print(f"\nContents of Silver table: {table}")
        try:
            spark.read.format("delta").load(path).show(truncate=False)
        except Exception as e:
            print(f"Error reading Silver table {table}: {e}")
    else:
        print(f"Silver table {table} does not exist at path: {path}")

print("\nFinished reading Silver tables.")
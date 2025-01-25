import os
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}/bin:" + os.environ["PATH"]

# Initialize SparkSession with Delta Lake support
builder = SparkSession.builder \
    .appName("Lakehouse Bronze Layer") \
    .master("local[1]") \
    .config("spark.sql.shuffle.partitions", "2") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Define paths dynamically relative to the script location
current_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
base_input_path = os.path.abspath(os.path.join(current_dir, "../../data/financial_services/datasets"))  # Normalize path
base_output_path = os.path.join(current_dir, "01-bronze")

# Ensure the output directory exists
os.makedirs(base_output_path, exist_ok=True)

# List of datasets
datasets = [
    "customers", "accounts", "transactions", "loans",
    "credit_cards", "branches", "compliance",
    "investments", "digital_activity"
]

# Process each dataset
for dataset in datasets:
    input_path = os.path.join(base_input_path, f"{dataset}.json")
    output_path = os.path.join(base_output_path, dataset)

    print(f"\nProcessing dataset: {dataset}")
    print(f"Input path: {input_path}")
    print(f"Output path: {output_path}")

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Warning: Dataset file not found: {input_path}. Skipping...")
        continue

    try:
        # Read JSON data with schema inference
        df = spark.read.option("multiline", "true").json(input_path)

        # Check if data is loaded successfully
        if df.head(1):
            print(f"Loaded {df.count()} rows from dataset: {dataset}")
            print(f"Sample data from {dataset}:")
            df.show(5)
        else:
            print(f"No data found in {dataset}. Skipping...")

        # Write data to Delta Lake (Bronze Layer)
        df.write.format("delta").mode("overwrite").save(output_path)
        print(f"Bronze data for {dataset} written to {output_path}")

    except Exception as e:
        print(f"Error processing {dataset}: {e}")

print("Bronze layer populated successfully.")
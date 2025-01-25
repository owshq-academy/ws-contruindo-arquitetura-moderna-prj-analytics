import pandas as pd
import os
import json

# Define the path to the analytical Parquet file
parquet_path = "/Users/mateusoliveira/Mateus/owshq/GitHub/ws-construindo-arq-modern-prj-analytics/demo/data-mesh/domain/analytical/credit_card_analytical_data.parquet"

# Check if the Parquet file exists
if not os.path.exists(parquet_path):
    raise FileNotFoundError(f"Parquet file not found: {parquet_path}")

# Read the Parquet file into a Pandas DataFrame
analytical_data = pd.read_parquet(parquet_path)

# Display a JSON-like preview of the first few rows
print("Analytical Data Preview (JSON Format):")
print(json.dumps(analytical_data.head(5).to_dict(orient="records"), indent=4))

# Perform basic analysis
total_cards = analytical_data.shape[0]
average_utilization_rate = analytical_data["credit_utilization_rate"].mean()
total_spent = analytical_data["total_spent"].sum()

# Display summary statistics in a simple JSON-like format
print("\nSummary Statistics:")
print(json.dumps({
    "Total Credit Cards": total_cards,
    "Average Credit Utilization Rate": round(average_utilization_rate, 2),
    "Total Spent": round(total_spent, 2)
}, indent=4))
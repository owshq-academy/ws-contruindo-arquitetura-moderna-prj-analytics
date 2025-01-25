import os
import pandas as pd
import random
import json

# Define paths
input_path = "/Users/mateusoliveira/Mateus/owshq/GitHub/ws-construindo-arq-modern-prj-analytics/data/financial_services/datasets/credit_cards.json"
output_path = "/Users/mateusoliveira/Mateus/owshq/GitHub/ws-construindo-arq-modern-prj-analytics/demo/data-mesh/domain/analytical/credit_card_analytical_data.parquet"

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Check if input file exists
if not os.path.exists(input_path):
    raise FileNotFoundError(f"Dataset file not found: {input_path}")

# Read raw data from JSON
try:
    with open(input_path, "r") as f:
        credit_cards = json.load(f)
except json.JSONDecodeError as e:
    raise ValueError(f"Error parsing JSON file: {e}")

# Validate credit card records
def validate_credit_card_data(card):
    required_fields = ["card_id", "customer_id", "credit_limit"]
    for field in required_fields:
        if field not in card:
            raise KeyError(f"Missing required field: {field}")
    if card["credit_limit"] <= 0:
        raise ValueError(f"Invalid credit limit: {card['credit_limit']}")

# Generate Analytical Data
def generate_analytical_data(credit_cards):
    validated_data = []
    for card in credit_cards:
        try:
            validate_credit_card_data(card)
            total_spent = round(random.uniform(1000, 20000), 2)
            credit_limit = card["credit_limit"]
            credit_utilization_rate = round(total_spent / credit_limit, 2) if credit_limit > 0 else 0.0
            validated_data.append({
                "card_id": card["card_id"],
                "customer_id": card["customer_id"],
                "total_spent": total_spent,
                "credit_limit": credit_limit,
                "credit_utilization_rate": credit_utilization_rate,
                "number_of_transactions": random.randint(10, 200)
            })
        except (KeyError, ValueError) as e:
            print(f"Skipping invalid record: {e}")
    return pd.DataFrame(validated_data)

# Generate the DataFrame and save to Parquet
try:
    analytical_data = generate_analytical_data(credit_cards)
    if analytical_data.empty:
        raise ValueError("No valid records to save.")
    analytical_data.to_parquet(output_path, index=False)
    print(f"Analytical data saved to {output_path}.")
except Exception as e:
    print(f"Error generating or saving analytical data: {e}")
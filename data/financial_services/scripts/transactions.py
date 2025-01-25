import random
from faker import Faker
import json

def generate_transactions(accounts, num_transactions_per_account=50):
    faker = Faker("pt_BR")
    data = []
    for account in accounts:
        for _ in range(random.randint(10, num_transactions_per_account)):
            transaction_id = faker.uuid4()
            transaction_type = random.choice(["Deposit", "Withdrawal", "Transfer", "Payment"])
            amount = round(random.uniform(10, 5000), 2)
            currency = "BRL"
            transaction_date = faker.date_time_this_year().isoformat()
            description = faker.sentence()
            data.append({
                "transaction_id": transaction_id,
                "account_id": account["account_id"],
                "transaction_type": transaction_type,
                "amount": amount,
                "currency": currency,
                "transaction_date": transaction_date,
                "description": description
            })
    return data

if __name__ == "__main__":
    with open("../datasets/accounts.json", "r") as f:
        accounts = json.load(f)
    transactions = generate_transactions(accounts)
    with open("../datasets/transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)
    print("Transaction data generated.")
import random
from faker import Faker
import json

def generate_accounts(customers, num_accounts_per_customer=2):
    faker = Faker("pt_BR")
    data = []
    for customer in customers:
        for _ in range(random.randint(1, num_accounts_per_customer)):
            account_id = faker.uuid4()
            account_type = random.choice(["Checking", "Savings", "Investment", "Business"])
            balance = round(random.uniform(100, 100000), 2)
            currency = "BRL"
            created_at = faker.date_time_this_decade()
            updated_at = faker.date_time_between_dates(datetime_start=created_at)
            data.append({
                "account_id": account_id,
                "customer_id": customer["customer_id"],
                "account_type": account_type,
                "balance": balance,
                "currency": currency,
                "created_at": created_at.isoformat(),
                "updated_at": updated_at.isoformat()
            })
    return data

if __name__ == "__main__":
    # Correct the file path here
    with open("../datasets/customers.json", "r") as f:
        customers = json.load(f)
    accounts = generate_accounts(customers)
    with open("../datasets/accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)
    print("Account data generated.")
import random
from faker import Faker
from dateutil.relativedelta import relativedelta
import json


def generate_investments(customers, accounts, num_investments_per_account=3):
    faker = Faker("pt_BR")
    data = []
    for account in accounts:
        for _ in range(random.randint(1, num_investments_per_account)):
            investment_id = faker.uuid4()
            customer_id = account["customer_id"]
            investment_type = random.choice(["Stocks", "Fixed Income", "Real Estate Funds"])
            amount = round(random.uniform(1000, 100000), 2)

            # Generate purchase_date as a datetime object
            purchase_date = faker.date_this_decade()
            # Safely add 5 years to purchase_date using relativedelta
            maturity_date = purchase_date + relativedelta(years=5)
            status = random.choice(["Active", "Closed"])

            data.append({
                "investment_id": investment_id,
                "customer_id": customer_id,
                "account_id": account["account_id"],
                "investment_type": investment_type,
                "amount": amount,
                "purchase_date": purchase_date.isoformat(),
                "maturity_date": maturity_date.isoformat(),
                "status": status
            })
    return data


if __name__ == "__main__":
    with open("../datasets/customers.json", "r") as f1, open("../datasets/accounts.json", "r") as f2:
        customers = json.load(f1)
        accounts = json.load(f2)
    investments = generate_investments(customers, accounts)
    with open("../datasets/investments.json", "w") as f:
        json.dump(investments, f, indent=4)
    print("Investment data generated.")
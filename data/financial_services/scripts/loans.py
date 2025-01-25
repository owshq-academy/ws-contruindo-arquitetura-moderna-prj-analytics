import random
from faker import Faker
from dateutil.relativedelta import relativedelta
import json


def generate_loans(customers, num_loans_per_customer=2):
    faker = Faker("pt_BR")
    data = []
    for customer in customers:
        for _ in range(random.randint(1, num_loans_per_customer)):
            loan_id = faker.uuid4()
            loan_type = random.choice(["Mortgage", "Auto", "Personal", "Business"])
            loan_amount = round(random.uniform(5000, 500000), 2)
            interest_rate = round(random.uniform(3, 15), 2)
            term = random.randint(12, 360)  # Loan term in months

            # Keep start_date as a datetime object
            start_date = faker.date_this_decade()
            # Safely calculate end_date using relativedelta
            end_date = start_date + relativedelta(months=term)

            loan_status = random.choice(["Active", "Paid Off", "Default"])
            data.append({
                "loan_id": loan_id,
                "customer_id": customer["customer_id"],
                "loan_type": loan_type,
                "loan_amount": loan_amount,
                "interest_rate": interest_rate,
                "term": term,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                "loan_status": loan_status
            })
    return data


if __name__ == "__main__":
    with open("../datasets/customers.json", "r") as f:
        customers = json.load(f)
    loans = generate_loans(customers)
    with open("../datasets/loans.json", "w") as f:
        json.dump(loans, f, indent=4)
    print("Loan data generated.")
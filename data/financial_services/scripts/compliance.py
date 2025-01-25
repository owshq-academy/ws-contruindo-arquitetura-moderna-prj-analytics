import random
from faker import Faker
import json

def generate_compliance(customers, num_records_per_customer=2):
    faker = Faker("pt_BR")
    data = []
    for customer in customers:
        for _ in range(random.randint(1, num_records_per_customer)):
            compliance_id = faker.uuid4()
            compliance_type = random.choice(["KYC", "AML", "LGPD"])
            status = random.choice(["Pending", "Completed", "Rejected"])
            review_date = faker.date_time_this_year().isoformat()
            comments = faker.sentence() if status == "Rejected" else ""
            data.append({
                "compliance_id": compliance_id,
                "customer_id": customer["customer_id"],
                "compliance_type": compliance_type,
                "status": status,
                "review_date": review_date,
                "comments": comments
            })
    return data

if __name__ == "__main__":
    with open("../datasets/customers.json", "r") as f:
        customers = json.load(f)
    compliance = generate_compliance(customers)
    with open("../datasets/compliance.json", "w") as f:
        json.dump(compliance, f, indent=4)
    print("Compliance data generated.")
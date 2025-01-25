from faker import Faker
import json
import random


def generate_customers(num_customers=10000):
    faker = Faker("pt_BR")
    data = []
    for _ in range(num_customers):
        customer_id = faker.uuid4()
        name = faker.name()
        email = faker.email()
        phone_number = faker.phone_number()
        address = faker.address().replace("\n", ", ")
        customer_type = random.choice(["Individual", "Business"])
        cpf = faker.cpf() if customer_type == "Individual" else ""
        cnpj = faker.cnpj() if customer_type == "Business" else ""

        # Keep created_at as a datetime object
        created_at = faker.date_time_this_decade()
        updated_at = faker.date_time_between_dates(datetime_start=created_at)

        data.append({
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "customer_type": customer_type,
            "cpf": cpf,
            "cnpj": cnpj,
            "created_at": created_at.isoformat(),
            "updated_at": updated_at.isoformat()
        })
    return data


if __name__ == "__main__":
    customers = generate_customers()
    with open("../datasets/customers.json", "w") as f:
        json.dump(customers, f, indent=4)
    print("Customer data generated.")
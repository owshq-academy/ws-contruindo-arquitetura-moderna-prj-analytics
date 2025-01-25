import random
from faker import Faker
import json


def generate_credit_cards(customers, num_cards_per_customer=2):
    faker = Faker("pt_BR")
    data = []
    for customer in customers:
        for _ in range(random.randint(1, num_cards_per_customer)):
            card_id = faker.uuid4()
            card_number = faker.credit_card_number()
            card_type = random.choice(["Visa", "MasterCard", "Elo"])
            expiry_date = faker.date_this_decade().isoformat()
            credit_limit = round(random.uniform(1000, 50000), 2)
            current_balance = round(random.uniform(0, credit_limit), 2)

            # Keep created_at and updated_at as datetime objects
            created_at = faker.date_time_this_decade()
            updated_at = faker.date_time_between_dates(datetime_start=created_at)

            data.append({
                "card_id": card_id,
                "customer_id": customer["customer_id"],
                "card_number": card_number,
                "card_type": card_type,
                "expiry_date": expiry_date,
                "credit_limit": credit_limit,
                "current_balance": current_balance,
                "created_at": created_at.isoformat(),
                "updated_at": updated_at.isoformat()
            })
    return data


if __name__ == "__main__":
    with open("../datasets/customers.json", "r") as f:
        customers = json.load(f)
    credit_cards = generate_credit_cards(customers)
    with open("../datasets/credit_cards.json", "w") as f:
        json.dump(credit_cards, f, indent=4)
    print("Credit card data generated.")
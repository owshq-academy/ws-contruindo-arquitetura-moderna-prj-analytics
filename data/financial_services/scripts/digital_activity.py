from faker import Faker
import json
import random

def generate_digital_activity(customers, num_activities_per_customer=5):
    faker = Faker("pt_BR")
    data = []
    for customer in customers:
        for _ in range(num_activities_per_customer):
            activity_id = faker.uuid4()
            activity_type = random.choice(["Login", "Transfer", "Payment"])
            timestamp = faker.date_time_this_year().isoformat()
            ip_address = faker.ipv4_public()
            device_type = random.choice(["Mobile", "Desktop", "Tablet"])
            data.append({
                "activity_id": activity_id,
                "customer_id": customer["customer_id"],
                "activity_type": activity_type,
                "timestamp": timestamp,
                "ip_address": ip_address,
                "device_type": device_type
            })
    return data

if __name__ == "__main__":
    with open("../datasets/customers.json", "r") as f:
        customers = json.load(f)
    activities = generate_digital_activity(customers)
    with open("../datasets/digital_activity.json", "w") as f:
        json.dump(activities, f, indent=4)
    print("Digital activity data generated.")
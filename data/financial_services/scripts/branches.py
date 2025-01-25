from faker import Faker
import json
from datetime import datetime


def generate_branches(num_branches=50):
    faker = Faker("pt_BR")
    data = []
    for _ in range(num_branches):
        branch_id = faker.uuid4()
        branch_name = faker.company()
        address = faker.address().replace("\n", ", ")
        phone_number = faker.phone_number()

        # Generate created_at as a datetime object
        created_at_dt = faker.date_time_this_decade()
        created_at = created_at_dt.isoformat()

        # Generate updated_at as a datetime object after created_at
        updated_at_dt = faker.date_time_between_dates(datetime_start=created_at_dt)
        updated_at = updated_at_dt.isoformat()

        data.append({
            "branch_id": branch_id,
            "branch_name": branch_name,
            "address": address,
            "phone_number": phone_number,
            "created_at": created_at,
            "updated_at": updated_at
        })
    return data


if __name__ == "__main__":
    branches = generate_branches()
    with open("../datasets/branches.json", "w") as f:
        json.dump(branches, f, indent=4, ensure_ascii=False)
    print("Branch data generated.")
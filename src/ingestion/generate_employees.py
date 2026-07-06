from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

os.makedirs("data/raw", exist_ok=True)

employees = []

positions = [
    "Store Manager",
    "Sales Associate",
    "Cashier",
    "Inventory Executive",
    "Customer Support"
]

for employee_id in range(1, 1001):
    employees.append({
        "employee_id": employee_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "position": random.choice(positions),
        "salary": random.randint(30000, 90000),
        "store_id": random.randint(1, 100)   # Foreign Key -> Stores
    })

df = pd.DataFrame(employees)

df.to_csv("data/raw/employees.csv", index=False)

print("✅ employees.csv generated successfully!")
print(df.head())
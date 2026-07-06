from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

os.makedirs("data/raw", exist_ok=True)

suppliers = []

for supplier_id in range(1, 501):
    suppliers.append({
        "supplier_id": supplier_id,
        "supplier_name": fake.company(),
        "contact_person": fake.name(),
        "email": fake.company_email(),
        "phone": fake.phone_number(),
        "city": fake.city(),
        "country": "USA"
    })

df = pd.DataFrame(suppliers)

df.to_csv("data/raw/suppliers.csv", index=False)

print("✅ suppliers.csv generated successfully!")
print(df.head())
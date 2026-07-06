from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

os.makedirs("data/raw", exist_ok=True)

stores = []

store_types = [
    "Supermarket",
    "Hypermarket",
    "Express",
    "Mall Outlet",
    "Warehouse"
]

for store_id in range(1, 101):
    stores.append({
        "store_id": store_id,
        "store_name": f"RetailSphere Store {store_id}",
        "store_type": random.choice(store_types),
        "city": fake.city(),
        "state": fake.state(),
        "country": "USA"
    })

df = pd.DataFrame(stores)

df.to_csv("data/raw/stores.csv", index=False)

print("✅ stores.csv generated successfully!")
print(df.head())
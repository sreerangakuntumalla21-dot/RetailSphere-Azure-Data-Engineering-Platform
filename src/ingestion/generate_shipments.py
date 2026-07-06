import pandas as pd
import random
import os
from datetime import datetime, timedelta

os.makedirs("data/raw", exist_ok=True)

shipments = []

start_date = datetime(2024, 1, 1)

for shipment_id in range(1, 10001):

    shipment_date = start_date + timedelta(days=random.randint(0, 730))

    shipments.append({
        "shipment_id": shipment_id,
        "supplier_id": random.randint(1, 500),
        "product_id": random.randint(1, 5000),
        "store_id": random.randint(1, 100),
        "shipment_date": shipment_date.strftime("%Y-%m-%d"),
        "quantity": random.randint(50, 1000)
    })

df = pd.DataFrame(shipments)

df.to_csv("data/raw/shipments.csv", index=False)

print("✅ shipments.csv generated successfully!")
print(df.head())
print(f"Total Shipments: {len(df)}")
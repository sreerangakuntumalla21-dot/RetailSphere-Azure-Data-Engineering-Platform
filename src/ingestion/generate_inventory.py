import pandas as pd
import random
import os

os.makedirs("data/raw", exist_ok=True)

inventory = []

inventory_id = 1

for store_id in range(1, 101):          # 100 stores
    for product_id in range(1, 5001):   # 5000 products

        inventory.append({
            "inventory_id": inventory_id,
            "store_id": store_id,
            "product_id": product_id,
            "stock_quantity": random.randint(0, 500),
            "reorder_level": random.randint(20, 100)
        })

        inventory_id += 1

df = pd.DataFrame(inventory)

df.to_csv("data/raw/inventory.csv", index=False)

print("✅ inventory.csv generated successfully!")
print(df.head())
print(f"Total Inventory Records: {len(df)}")
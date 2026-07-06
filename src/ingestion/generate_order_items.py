import pandas as pd
import random
import os

os.makedirs("data/raw", exist_ok=True)

order_items = []

order_item_id = 1

for order_id in range(1, 50001):

    # Each order has between 1 and 5 products
    number_of_products = random.randint(1, 5)

    for _ in range(number_of_products):

        quantity = random.randint(1, 5)
        unit_price = round(random.uniform(10, 2000), 2)

        order_items.append({
            "order_item_id": order_item_id,
            "order_id": order_id,
            "product_id": random.randint(1, 5000),
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": round(quantity * unit_price, 2)
        })

        order_item_id += 1

df = pd.DataFrame(order_items)

df.to_csv("data/raw/order_items.csv", index=False)

print("✅ order_items.csv generated successfully!")
print(df.head())
print(f"\nTotal Order Items: {len(df)}")
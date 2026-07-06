from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

os.makedirs("data/raw", exist_ok=True)

categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Sports",
    "Books",
    "Beauty",
    "Toys",
    "Furniture",
    "Groceries",
    "Automotive"
]

products = []

for product_id in range(1, 5001):
    category = random.choice(categories)

    products.append({
        "product_id": product_id,
        "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "category": category,
        "brand": fake.company(),
        "price": round(random.uniform(10, 2000), 2),
        "stock_quantity": random.randint(10, 1000)
    })

df = pd.DataFrame(products)

df.to_csv("data/raw/products.csv", index=False)

print("✅ products.csv generated successfully!")
print(df.head())
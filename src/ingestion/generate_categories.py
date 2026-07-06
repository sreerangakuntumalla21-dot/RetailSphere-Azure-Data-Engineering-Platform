import pandas as pd
import os

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

category_data = []

for i, category in enumerate(categories, start=1):
    category_data.append({
        "category_id": i,
        "category_name": category
    })

df = pd.DataFrame(category_data)

df.to_csv("data/raw/categories.csv", index=False)

print("✅ categories.csv generated successfully!")
print(df)
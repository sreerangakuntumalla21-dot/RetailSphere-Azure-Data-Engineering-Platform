from faker import Faker
import pandas as pd
import random
import os
from datetime import datetime, timedelta

fake = Faker()

os.makedirs("data/raw", exist_ok=True)

orders = []

start_date = datetime(2024, 1, 1)

for order_id in range(1, 50001):

    order_date = start_date + timedelta(days=random.randint(0, 730))

    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1, 1000),   # FK -> Customers
        "store_id": random.randint(1, 100),        # FK -> Stores
        "employee_id": random.randint(1, 1000),    # FK -> Employees
        "order_date": order_date.strftime("%Y-%m-%d"),
        "payment_method": random.choice([
            "Cash",
            "Credit Card",
            "Debit Card",
            "UPI",
            "Net Banking"
        ]),
        "order_status": random.choice([
            "Completed",
            "Pending",
            "Cancelled",
            "Returned"
        ])
    })

df = pd.DataFrame(orders)

df.to_csv("data/raw/orders.csv", index=False)

print("✅ orders.csv generated successfully!")
print(df.head())
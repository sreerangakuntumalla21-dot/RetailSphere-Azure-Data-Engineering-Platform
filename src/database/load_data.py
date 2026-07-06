import pandas as pd
from db_connection import get_connection

DATASETS = {
    "customers": "data/raw/customers.csv",
    "categories": "data/raw/categories.csv",
    "products": "data/raw/products.csv",
    "stores": "data/raw/stores.csv",
    "employees": "data/raw/employees.csv",
    "suppliers": "data/raw/suppliers.csv",
    "orders": "data/raw/orders.csv",
    "order_items": "data/raw/order_items.csv",
    "inventory": "data/raw/inventory.csv",
    "shipments": "data/raw/shipments.csv"
}

conn = get_connection()

if conn:

    cursor = conn.cursor()

    for table, file_path in DATASETS.items():

        print(f"\nLoading {table}...")

        df = pd.read_csv(file_path)

        columns = ",".join(df.columns)

        placeholders = ",".join(["%s"] * len(df.columns))

        query = f"""
        INSERT INTO {table} ({columns})
        VALUES ({placeholders})
        """

        for row in df.itertuples(index=False):
            cursor.execute(query, tuple(row))

        conn.commit()

        print(f"✅ {table} loaded successfully.")

    cursor.close()
    conn.close()

    print("\n🎉 All datasets loaded successfully!")
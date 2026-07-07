from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, col


spark = (
    SparkSession.builder
    .appName("RetailSphere Dashboard Dataset")
    .getOrCreate()
)


orders = spark.read.csv(
    "data/raw/orders.csv",
    header=True,
    inferSchema=True
)

order_items = spark.read.csv(
    "data/raw/order_items.csv",
    header=True,
    inferSchema=True
)

products = spark.read.csv(
    "data/raw/products.csv",
    header=True,
    inferSchema=True
)

stores = spark.read.csv(
    "data/raw/stores.csv",
    header=True,
    inferSchema=True
)

customers = spark.read.csv(
    "data/raw/customers.csv",
    header=True,
    inferSchema=True
)


dashboard = (
    orders
    .join(order_items, "order_id")
    .join(products, "product_id")
    .join(stores, "store_id")
    .join(customers, "customer_id")
)

print("Dashboard Dataset Created Successfully")

dashboard.show(10, truncate=False)

print(f"Total Records : {dashboard.count()}")

spark.stop()
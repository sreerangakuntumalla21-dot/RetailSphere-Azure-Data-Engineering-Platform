from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, col


spark = (
    SparkSession.builder
    .appName("Customer Analytics")
    .getOrCreate()
)


customers = spark.read.csv(
    "data/raw/customers.csv",
    header=True,
    inferSchema=True
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


sales = orders.join(order_items, "order_id")


customer_sales = sales.join(customers, "customer_id")


analytics = (
    customer_sales
    .groupBy(
        "customer_id",
        "first_name",
        "last_name"
    )
    .agg(
        count("order_id").alias("total_orders"),
        sum("total_price").alias("total_spent")
    )
    .orderBy(col("total_spent").desc())
)

print("========== TOP 10 CUSTOMERS ==========")

analytics.show(10, truncate=False)

spark.stop()
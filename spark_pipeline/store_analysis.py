from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, col

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("Store Performance Analysis")
    .getOrCreate()
)

# Read Data
stores = spark.read.csv(
    "data/raw/stores.csv",
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

# Join tables
sales = (
    orders
    .join(order_items, "order_id")
    .join(stores, "store_id")
)

# Store KPIs
store_performance = (
    sales
    .groupBy(
        "store_id",
        "store_name",
        "city",
        "state"
    )
    .agg(
        count("order_id").alias("total_orders"),
        sum("total_price").alias("total_sales")
    )
    .orderBy(col("total_sales").desc())
)

print("========== TOP 10 STORES ==========")

store_performance.show(10, truncate=False)

spark.stop()
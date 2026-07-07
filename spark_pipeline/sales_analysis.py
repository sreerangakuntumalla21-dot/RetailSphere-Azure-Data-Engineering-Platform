from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

spark = (
    SparkSession.builder
    .appName("RetailSphere Sales Analysis")
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


sales = orders.join(order_items, "order_id")


sales_summary = (
    sales.groupBy("order_id")
         .agg(sum("total_price").alias("total_sales"))
         .orderBy(col("total_sales").desc())
)

print("Top 10 Orders by Sales")

sales_summary.show(10)

spark.stop()
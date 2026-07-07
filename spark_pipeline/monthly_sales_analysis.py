from pyspark.sql import SparkSession
from pyspark.sql.functions import month, year, sum, col


spark = (
    SparkSession.builder
    .appName("Monthly Sales Analysis")
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

# Extract Year and Month
sales = (
    sales
    .withColumn("year", year(col("order_date")))
    .withColumn("month", month(col("order_date")))
)


monthly_sales = (
    sales
    .groupBy("year", "month")
    .agg(
        sum("total_price").alias("monthly_revenue")
    )
    .orderBy("year", "month")
)

print("========== MONTHLY SALES ==========")

monthly_sales.show(24, truncate=False)

spark.stop()
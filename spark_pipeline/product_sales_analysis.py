from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("Product Sales Analysis")
    .getOrCreate()
)

# Read Data
products = spark.read.csv(
    "data/raw/products.csv",
    header=True,
    inferSchema=True
)

order_items = spark.read.csv(
    "data/raw/order_items.csv",
    header=True,
    inferSchema=True
)

# Join Products with Order Items
sales = order_items.join(products, "product_id")

# Calculate Total Sales Per Product
product_sales = (
    sales.groupBy(
        "product_id",
        "product_name"
    )
    .agg(
        sum("total_price").alias("total_sales")
    )
    .orderBy(col("total_sales").desc())
)

print("========== TOP 10 PRODUCTS ==========")

product_sales.show(10, truncate=False)

spark.stop()
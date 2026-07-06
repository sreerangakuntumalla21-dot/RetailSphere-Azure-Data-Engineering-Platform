from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("RetailSphere Big Data Platform")
    .master("local[*]")
    .getOrCreate()
)

print("✅ Spark Session Created Successfully")
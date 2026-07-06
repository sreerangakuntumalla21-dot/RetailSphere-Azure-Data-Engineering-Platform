from pyspark.sql import SparkSession

def get_spark():

    spark = (
        SparkSession.builder
        .appName("RetailSphere Analytics Platform")
        .master("local[*]")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark
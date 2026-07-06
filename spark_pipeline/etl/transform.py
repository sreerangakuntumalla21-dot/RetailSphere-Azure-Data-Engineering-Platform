from pyspark.sql.functions import col, when

def transform_customers(customers):

    customers = customers.withColumn(
        "age_group",
        when(col("age") < 30, "Young")
        .when(col("age") < 50, "Adult")
        .otherwise("Senior")
    )

    return customers
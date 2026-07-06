from pyspark.sql.functions import month, year, sum


def monthly_sales(orders, order_items):

    # Join Orders and Order Items
    sales = orders.join(
        order_items,
        "order_id"
    )

    # Create monthly summary
    monthly = (
        sales
        .withColumn("Year", year("order_date"))
        .withColumn("Month", month("order_date"))
        .groupBy("Year", "Month")
        .agg(
            sum("total_price").alias("Monthly Sales")
        )
        .orderBy("Year", "Month")
    )

    return monthly
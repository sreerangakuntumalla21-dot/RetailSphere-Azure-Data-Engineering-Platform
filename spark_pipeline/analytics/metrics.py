from pyspark.sql.functions import sum, count, avg


def calculate_kpis(data):

    order_items = data["order_items"]
    customers = data["customers"]
    products = data["products"]
    stores = data["stores"]

    total_revenue = order_items.select(
        sum("total_price").alias("Total Revenue")
    )

    total_orders = order_items.select(
        count("order_id").alias("Total Orders")
    )

    average_order = order_items.select(
        avg("total_price").alias("Average Order Value")
    )

    total_customers = customers.select(
        count("customer_id").alias("Total Customers")
    )

    total_products = products.select(
        count("product_id").alias("Total Products")
    )

    total_stores = stores.select(
        count("store_id").alias("Total Stores")
    )

    return {
        "revenue": total_revenue,
        "orders": total_orders,
        "average_order": average_order,
        "customers": total_customers,
        "products": total_products,
        "stores": total_stores
    }
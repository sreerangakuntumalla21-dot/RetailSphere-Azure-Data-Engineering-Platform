from spark_pipeline.config.spark_config import get_spark

# Create Spark Session
spark = get_spark()


def extract_all_data():
    """
    Read all datasets from the raw data folder
    and return them as a dictionary.
    """

    datasets = {
        "customers": spark.read.csv(
            "data/raw/customers.csv",
            header=True,
            inferSchema=True
        ),

        "products": spark.read.csv(
            "data/raw/products.csv",
            header=True,
            inferSchema=True
        ),

        "categories": spark.read.csv(
            "data/raw/categories.csv",
            header=True,
            inferSchema=True
        ),

        "stores": spark.read.csv(
            "data/raw/stores.csv",
            header=True,
            inferSchema=True
        ),

        "employees": spark.read.csv(
            "data/raw/employees.csv",
            header=True,
            inferSchema=True
        ),

        "suppliers": spark.read.csv(
            "data/raw/suppliers.csv",
            header=True,
            inferSchema=True
        ),

        "orders": spark.read.csv(
            "data/raw/orders.csv",
            header=True,
            inferSchema=True
        ),

        "order_items": spark.read.csv(
            "data/raw/order_items.csv",
            header=True,
            inferSchema=True
        ),

        "inventory": spark.read.csv(
            "data/raw/inventory.csv",
            header=True,
            inferSchema=True
        ),

        "shipments": spark.read.csv(
            "data/raw/shipments.csv",
            header=True,
            inferSchema=True
        )
    }

    print("✅ All datasets loaded successfully!")

    return datasets
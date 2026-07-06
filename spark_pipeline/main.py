from spark_pipeline.etl.extract import extract_all_data
from spark_pipeline.etl.transform import transform_customers
from spark_pipeline.analytics.metrics import calculate_kpis
from spark_pipeline.analytics.kpi_dashboard import create_kpi_dashboard
from spark_pipeline.etl.load import export_csv
from spark_pipeline.config.spark_config import get_spark
from spark_pipeline.analytics.monthly_sales import monthly_sales


def main():

    print("=" * 60)
    print("RetailSphere Pipeline Started")
    print("=" * 60)

    # Create Spark Session
    spark = get_spark()

    # -----------------------------
    # Extract
    # -----------------------------
    data = extract_all_data()

    # -----------------------------
    # Transform
    # -----------------------------
    customers = transform_customers(
        data["customers"]
    )

    # Update transformed dataframe
    data["customers"] = customers

    # -----------------------------
    # Analytics
    # -----------------------------
    kpis = calculate_kpis(data)

    print("\n========== KPI REPORT ==========\n")

    print("Total Revenue")
    kpis["revenue"].show()

    print("Total Orders")
    kpis["orders"].show()

    print("Average Order Value")
    kpis["average_order"].show()

    print("Total Customers")
    kpis["customers"].show()

    print("Total Products")
    kpis["products"].show()

    print("Total Stores")
    kpis["stores"].show()

    # -----------------------------
    # Dashboard Dataset
    # -----------------------------
    dashboard = create_kpi_dashboard(kpis)

    export_csv(
        dashboard,
        "kpi_dashboard.csv"
    )

    monthly = monthly_sales(
        data["orders"],
        data["order_items"]
    )

    export_csv(
        monthly,
        "monthly_sales.csv"
    )

    print("\n✅ Pipeline Finished Successfully!")

    spark.stop()


if __name__ == "__main__":
    main()
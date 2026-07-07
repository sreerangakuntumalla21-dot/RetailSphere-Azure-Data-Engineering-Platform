# RetailSphere - ETL Pipeline

## Pipeline Flow

CSV Files
      │
      ▼
Extract
      │
      ▼
Transform
      │
      ▼
Analytics
      │
      ▼
Load
      │
      ▼
Power BI Dashboard

---

## Extract

The Extract module reads all retail datasets into PySpark DataFrames.

Datasets:
- Customers
- Orders
- Order Items
- Products
- Categories
- Stores
- Inventory
- Suppliers
- Employees
- Shipments

---

## Transform

Business transformations include:

- Data cleaning
- Null handling
- Customer age grouping
- Data validation
- Column selection

---

## Analytics

The Analytics module calculates business KPIs.

KPIs:
- Total Revenue
- Total Orders
- Average Order Value
- Total Customers
- Total Products
- Total Stores
- Monthly Sales

---

## Load

The Load module exports analytics datasets as CSV files.

Generated Outputs

- kpi_dashboard.csv
- monthly_sales.csv

These files are used directly in Power BI for visualization.

---

## Pipeline Execution

Run the complete pipeline using:

```bash
python -m spark_pipeline.main
```

The pipeline performs:

1. Extract data
2. Transform data
3. Calculate KPIs
4. Export analytics datasets
5. Visualize insights in Power BI

---

## Technologies

- Python
- PySpark
- PostgreSQL
- SQL
- Power BI
- Git
- GitHub
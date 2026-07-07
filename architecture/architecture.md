# RetailSphere - System Architecture

## Overview

RetailSphere is an end-to-end Data Engineering Platform designed to simulate a real-world retail analytics system. The project demonstrates how raw retail data flows through an ETL pipeline before being transformed into business insights using Power BI.

---

## Architecture

Raw Data (CSV Files)
        │
        ▼
Python Data Generation
        │
        ▼
PostgreSQL Database
        │
        ▼
PySpark ETL Pipeline
 ├── Extract
 ├── Transform
 ├── Analytics
 └── Load
        │
        ▼
Analytics Output (CSV)
        │
        ▼
Power BI Dashboard

---

## Components

### Data Generation
- Synthetic retail datasets generated using Python
- Customers
- Orders
- Products
- Stores
- Inventory
- Suppliers
- Employees
- Shipments

### Database
- PostgreSQL stores enterprise retail data.
- Tables are normalized using primary and foreign keys.

### ETL Pipeline
The PySpark pipeline follows a modular architecture:

- Extract
- Transform
- Analytics
- Load

### Reporting
Power BI visualizes KPIs such as:
- Total Revenue
- Monthly Sales
- Total Orders
- Customers
- Products
- Stores

---

## Technologies

- Python
- PySpark
- PostgreSQL
- SQL
- Power BI
- Git
- GitHub
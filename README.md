# 🛒 RetailSphere – Enterprise Retail Data Engineering Platform

> End-to-End Enterprise Data Engineering Project using Python, PostgreSQL, Azure, ETL, and Power BI.

---

# 📌 Project Overview

RetailSphere is a production-style data engineering project that simulates how a retail company collects, processes, stores, and analyzes enterprise-scale data.

The project demonstrates the complete data engineering lifecycle—from generating raw transactional data to building an automated ETL pipeline, storing it in PostgreSQL, and preparing it for cloud analytics using Microsoft Azure.

---

# 🎯 Business Problem

Retail companies generate millions of records every day from:

- Customer registrations
- Product catalogs
- Store operations
- Sales transactions
- Inventory management
- Supplier shipments

The objective is to build a scalable, automated data platform that transforms raw operational data into analytics-ready datasets.

---

# 🏗️ Solution Architecture

```text
Raw CSV Data
      │
      ▼
Python Data Generation
      │
      ▼
PostgreSQL Database
      │
      ▼
Python ETL Pipeline
      │
      ▼
Azure Data Lake (Bronze)
      │
      ▼
Azure Databricks (Silver)
      │
      ▼
Gold Layer
      │
      ▼
Azure Synapse Analytics
      │
      ▼
Power BI Dashboard
```

---

# 🛠️ Tech Stack

### Programming

- Python
- SQL

### Database

- PostgreSQL

### Data Processing

- Pandas
- Faker
- psycopg2

### Cloud (Upcoming)

- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks (PySpark)
- Azure Synapse Analytics

### Visualization

- Power BI

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
RetailSphere-Azure-Data-Engineering-Platform/

├── architecture/
├── config/
├── data/
├── docs/
├── logs/
├── notebooks/
├── powerbi/
├── screenshots/
├── sql/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Enterprise Datasets

| Dataset | Records |
|----------|---------:|
| Customers | 1,000 |
| Categories | 10 |
| Products | 5,000 |
| Stores | 100 |
| Employees | 1,000 |
| Suppliers | 500 |
| Orders | 50,000 |
| Order Items | 150,000+ |
| Inventory | 500,000 |
| Shipments | 10,000 |

---

# ⚙️ Features

- Enterprise-scale synthetic data generation
- Relational PostgreSQL database
- Automated ETL pipeline
- SQL scripts for schema creation
- Foreign key relationships
- Data validation
- Modular Python code
- Scalable architecture

---

# 🚀 Current Progress

- ✅ Enterprise Data Generation
- ✅ PostgreSQL Database
- ✅ SQL Schema
- ✅ ETL Pipeline
- 🔄 Azure Migration (In Progress)
- ⏳ Azure Data Factory
- ⏳ Azure Databricks
- ⏳ Azure Synapse
- ⏳ Power BI Dashboard

---

# 📈 Future Enhancements

- Incremental Data Loading
- ETL Logging
- Data Quality Validation
- Azure Data Factory Pipelines
- Azure Databricks (PySpark)
- Azure Synapse Analytics
- Power BI Dashboard
- GitHub Actions CI/CD

---

# 👨‍💻 Author

**Sreeranga Kuntumalla**

Data Engineer | Python | SQL | PostgreSQL | Azure | Power BI
# RetailSphere Enterprise Architecture

## Overview

RetailSphere follows a modern enterprise data engineering architecture.

```text
                Raw CSV Files
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
      Azure Data Lake Storage (Bronze)
                      │
                      ▼
     Azure Databricks Transformations
                      │
                      ▼
           Silver Layer (Clean Data)
                      │
                      ▼
        Gold Layer (Business Ready)
                      │
                      ▼
          Azure Synapse Analytics
                      │
                      ▼
             Power BI Dashboards
```
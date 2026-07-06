import pandas as pd


def create_kpi_dashboard(kpis):

    dashboard = pd.DataFrame({
        "Total Revenue": [float(kpis["revenue"].collect()[0][0])],
        "Total Orders": [int(kpis["orders"].collect()[0][0])],
        "Average Order Value": [float(kpis["average_order"].collect()[0][0])],
        "Total Customers": [int(kpis["customers"].collect()[0][0])],
        "Total Products": [int(kpis["products"].collect()[0][0])],
        "Total Stores": [int(kpis["stores"].collect()[0][0])]
    })

    return dashboard
import pandas as pd

# Task 1: Data Ingestion & Cleaning (1 Mark)
df = pd.read_csv('archive/online_retail.csv', parse_dates=['InvoiceDate'])
df = df.dropna(subset=['CustomerID'])

# Task 2: Feature Engineering (1 Mark)
df['Revenue'] = df['Quantity'] * df['UnitPrice']
# Extract year-month period 
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M') 

# Task 3: Grouping & Aggregation (2 Marks)
# Using named aggregation to assign the specific column names requested
monthly_stats = df.groupby('YearMonth').agg(
    TotalRevenue=('Revenue', 'sum'),
    UniqueCustomers=('CustomerID', 'nunique')
).reset_index()

# Task 4: Filtering & File Output (2 Marks)
top_months = monthly_stats[monthly_stats['TotalRevenue'] > 500000]
top_months.to_csv('top_performing_months.csv', index=False)

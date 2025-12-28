import pandas as pd

# Read data
file_path = 'data/Database-Q3_2020.xlsx'
df_mkt = pd.read_excel(file_path, sheet_name='MKT')
df_sales = pd.read_excel(file_path, sheet_name='Sales')

# Marketer Performance (from MKT sheet)
marketer_stats = df_mkt.groupby('MKTer').agg({
    'Chi phí Marketing': 'sum',
    'Doanh thu': 'sum',
    'Lead MKT': 'sum'
}).reset_index()

# Calculate ROAS for each Marketer
marketer_stats['ROAS'] = marketer_stats['Doanh thu'] / marketer_stats['Chi phí Marketing']
marketer_stats = marketer_stats.sort_values('Doanh thu', ascending=False)

print("Marketer Performance (Top 5 by Revenue):")
print(marketer_stats.head())

# Sales Performance (from Sales sheet)
sales_stats = df_sales.groupby('Sales').agg({
    'Tổng tiền': 'sum',
    'Số lần tương tác': 'mean'
}).reset_index()

sales_stats = sales_stats.sort_values('Tổng tiền', ascending=False)

print("\nSales Performance (Top 5 by Revenue):")
print(sales_stats.head())

# Save results
marketer_stats.to_csv('data/analyze/marketer_performance.csv', index=False)
sales_stats.to_csv('data/analyze/sales_performance.csv', index=False)
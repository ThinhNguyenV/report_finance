import pandas as pd
import matplotlib.pyplot as plt

# Load data from 'MKT' and 'Sales' worksheets
file_path = 'data/Database-Q3_2020.xlsx'
df_mkt = pd.read_excel(file_path, sheet_name='MKT')
df_sales = pd.read_excel(file_path, sheet_name='Sales')

# Convert date columns to datetime format
df_mkt['Date'] = pd.to_datetime(df_mkt['Date'])
df_sales['Ngày gọi'] = pd.to_datetime(df_sales['Ngày gọi'])

# Aggregate revenue and costs by day from the MKT table
daily_mkt = df_mkt.groupby('Date').agg({
    'Chi phí Marketing': 'sum',
    'Doanh thu': 'sum',
    'Paid Revenue 1': 'sum'
}).reset_index()

# Aggregate revenue from the Sales table (based on 'Tổng tiền' and 'Ngày gọi')
daily_sales = df_sales.groupby('Ngày gọi').agg({
    'Tổng tiền': 'sum'
}).reset_index()

# Rename columns for consistency during merge
daily_sales.rename(columns={'Ngày gọi': 'Date', 'Tổng tiền': 'Sales_Revenue'}, inplace=True)

# Combine data from both sources using an outer join
df_combined = pd.merge(daily_mkt, daily_sales, on='Date', how='outer').fillna(0)
df_combined = df_combined.sort_values('Date')

# Save the preliminary analysis results to CSV
df_combined.to_csv('daily_finance_summary.csv', index=False)

# Plot revenue and cost trends
plt.figure(figsize=(12, 6))
plt.plot(df_combined['Date'], df_combined['Doanh thu'], label='Revenue (MKT)')
plt.plot(df_combined['Date'], df_combined['Chi phí Marketing'], label='Marketing Cost')
plt.title('Q3 2020 Financial Trends')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.savefig('predict/finance_trend.png')

print("Data has been saved to daily_finance_summary.csv and the chart to finance_trend.png")
print(df_combined.head())
print(df_combined.describe())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
file_path = 'data/Database-Q3_2020.xlsx'
df_mkt = pd.read_excel(file_path, sheet_name='MKT')

# Data cleaning: remove rows with 0 cost or revenue to analyze actual correlation
df_clean = df_mkt[(df_mkt['Chi phí Marketing'] > 0) & (df_mkt['Doanh thu'] > 0)].copy()

# Calculate correlation coefficients
correlation = df_clean[['Chi phí Marketing', 'Doanh thu', 'Lead MKT', 'Đơn hàng']].corr()

print("Correlation coefficients between key variables:")
print(correlation)

# Plot Scatter Plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Chi phí Marketing', y='Doanh thu', data=df_clean, scatter_kws={'alpha':0.5})
plt.title('Correlation between Marketing Cost and Revenue')
plt.xlabel('Marketing Cost (VND)')
plt.ylabel('Revenue (VND)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('model/analyze/img/correlation_mkt_revenue.png')

# Calculate average ROAS (Return on Ad Spend)
df_clean['ROAS'] = df_clean['Doanh thu'] / df_clean['Chi phí Marketing']
print(f"\nAverage ROAS: {df_clean['ROAS'].mean():.2f}")
print(f"Median ROAS: {df_clean['ROAS'].median():.2f}")

# Save results
df_clean.to_csv('data/analyze/mkt_efficiency_analysis.csv', index=False)
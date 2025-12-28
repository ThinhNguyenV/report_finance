import pandas as pd
import numpy as np

# Load aggregated data
df = pd.read_csv('data/model/daily_finance_summary.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Set Date as the index
df.set_index('Date', inplace=True)

# Create time-series features
df['day_of_week'] = df.index.dayofweek
df['day_of_month'] = df.index.day
df['month'] = df.index.month

# Create lag features for Revenue (Doanh thu)
# This helps the model learn from past patterns (previous 7 days)
for i in range(1, 8):
    df[f'revenue_lag_{i}'] = df['Doanh thu'].shift(i)

# Create a 7-day rolling mean
# Uses the average of the previous week to capture trends
df['revenue_rolling_mean_7'] = df['Doanh thu'].shift(1).rolling(window=7).mean()

# Drop rows with NaN values caused by generating lag/rolling features
df_model = df.dropna()

# Save the preprocessed data for modeling
df_model.to_csv('data/preprocessed_finance_data.csv')

print("Preprocessing complete. Data saved to 'data/preprocessed_finance_data.csv'.")
print("\n--- Preview of Preprocessed Data (First 5 rows) ---")
print(df_model.head())
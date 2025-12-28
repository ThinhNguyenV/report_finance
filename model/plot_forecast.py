import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load historical data
df_history = pd.read_csv('data/daily_finance_summary.csv')
df_history['Date'] = pd.to_datetime(df_history['Date'])

# Load forecasted data
df_forecast = pd.read_csv('data/finance_forecast_next_month.csv')
df_forecast['Date'] = pd.to_datetime(df_forecast['Date'])
df_forecast.rename(columns={'Forecasted_Revenue': 'Doanh thu'}, inplace=True)

# Combine historical and forecasted data
df_combined = pd.concat([df_history[['Date', 'Doanh thu']], df_forecast[['Date', 'Doanh thu']]])

# Initialize the plot
plt.figure(figsize=(14, 7))
plt.plot(df_history['Date'], df_history['Doanh thu'], label='Historical Revenue (Q3 2020)', color='blue')
plt.plot(df_forecast['Date'], df_forecast['Doanh thu'], label='Forecasted Revenue (Next Month)', color='red', linestyle='--')

# Add a vertical line to separate historical and forecasted data
plt.axvline(x=df_history['Date'].max(), color='gray', linestyle=':', linewidth=1, label='Last Day of Historical Data')

# Chart formatting
plt.title('Historical vs Forecasted Revenue Trends', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue (VND)', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()

# Format y-axis for better readability (showing in Millions)
def format_y_axis(value, tick_number):
    return f'{value/1e6:,.0f}M'

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_y_axis))

# Save the combined trend chart
plt.savefig('predict/finance_forecast_combined_trend.png')

print("Combined chart has been saved to finance_forecast_combined_trend.png")
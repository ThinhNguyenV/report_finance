import pandas as pd
import joblib
import numpy as np
from datetime import timedelta

# Load preprocessed data and the trained model
df = pd.read_csv('data/preprocessed_finance_data.csv', index_col='Date')
df.index = pd.to_datetime(df.index)
model = joblib.load('model/finance_forecast_model.pkl')

# Get the last available date in the dataset to start the forecast
last_date = df.index.max()
forecast_dates = [last_date + timedelta(days=i) for i in range(1, 31)]

# Prepare data for daily recursive forecasting
# We use the last row of existing data to start generating lag features
current_data = df.iloc[-1:].copy()
forecast_results = []

for date in forecast_dates:
    # Generate features for the specific forecast date
    # Note: 'Doanh thu' is used as the target variable from previous predictions
    features = {
        'day_of_week': date.dayofweek,
        'day_of_month': date.day,
        'month': date.month,
        'revenue_lag_1': current_data['Doanh thu'].iloc[-1],
        'revenue_lag_2': current_data['revenue_lag_1'].iloc[-1],
        'revenue_lag_3': current_data['revenue_lag_2'].iloc[-1],
        'revenue_lag_4': current_data['revenue_lag_3'].iloc[-1],
        'revenue_lag_5': current_data['revenue_lag_4'].iloc[-1],
        'revenue_lag_6': current_data['revenue_lag_5'].iloc[-1],
        'revenue_lag_7': current_data['revenue_lag_6'].iloc[-1],
        'revenue_rolling_mean_7': np.mean([
            current_data['Doanh thu'].iloc[-1],
            current_data['revenue_lag_1'].iloc[-1],
            current_data['revenue_lag_2'].iloc[-1],
            current_data['revenue_lag_3'].iloc[-1],
            current_data['revenue_lag_4'].iloc[-1],
            current_data['revenue_lag_5'].iloc[-1],
            current_data['revenue_lag_6'].iloc[-1]
        ])
    }
    
    # Create a DataFrame for the current prediction step
    X_pred = pd.DataFrame([features])
    pred_revenue = model.predict(X_pred)[0]
    
    # Store the forecast result
    forecast_results.append({'Date': date, 'Forecasted_Revenue': pred_revenue})
    
    # Update current_data to feed the next loop iteration (Recursive Step)
    new_row = pd.DataFrame({
        'Doanh thu': [pred_revenue],
        'revenue_lag_1': [features['revenue_lag_1']],
        'revenue_lag_2': [features['revenue_lag_2']],
        'revenue_lag_3': [features['revenue_lag_3']],
        'revenue_lag_4': [features['revenue_lag_4']],
        'revenue_lag_5': [features['revenue_lag_5']],
        'revenue_lag_6': [features['revenue_lag_6']],
        'revenue_lag_7': [features['revenue_lag_7']]
    }, index=[date])
    current_data = pd.concat([current_data, new_row])

# Save forecast results to CSV
forecast_df = pd.DataFrame(forecast_results)
forecast_df.to_csv('data/data_model/finance_forecast_next_month.csv', index=False)

print("Forecast for the next month has been completed.")
print("\n--- Forecast Preview (First 5 Days) ---")
print(forecast_df.head())
print(f"\nTotal forecasted revenue for the next month: {forecast_df['Forecasted_Revenue'].sum():,.0f}")
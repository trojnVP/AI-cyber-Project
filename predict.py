import pandas as pd
import joblib
import os

# Define the path to the data
data_path = r'C:\Users\admin\Desktop\cyber project final\data\prepared_data.csv'

# Load the saved model and label encoder
model = joblib.load('models/random_forest_model.pkl')
feature_columns = joblib.load('models/feature_columns.pkl')
encoder = joblib.load('models/label_encoder_country.pkl')

# Load the prepared data
df = pd.read_csv(data_path)

# Drop irrelevant columns if still present
columns_to_drop = ['ipAddress', 'domain', 'isp', 'lastReportedAt']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Encode 'countryCode' using the saved label encoder
df['countryCode'] = encoder.transform(df['countryCode'])

# Remove target column if present
if 'is_malicious' in df.columns:
    df = df.drop(columns=['is_malicious'])

# Ensure correct column order
df = df[feature_columns]

# Predict using the model
predictions = model.predict(df)

# Add predictions to DataFrame
df['Prediction'] = ['Benign' if pred == 0 else 'Malicious' for pred in predictions]

# Print first 10 results
print(df[['Prediction']].head(10))

# Save results
output_path = r'C:\Users\admin\Desktop\cyber project final\data\predictions_output.csv'
df.to_csv(output_path, index=False)
print(f"\nPredictions saved to: {output_path}")

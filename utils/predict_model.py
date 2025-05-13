import pandas as pd
import joblib
import os

# Load the trained model and feature column order
model = joblib.load('models/random_forest_model.pkl')
feature_columns = joblib.load('models/feature_columns.pkl')
encoder = joblib.load('models/label_encoder_country.pkl')

# Load the dataset to predict on
data_path = 'C:/Users/admin/Desktop/cyber project final/data/prepared_data.csv'
df = pd.read_csv(data_path)

# Drop unused or non-numeric columns
columns_to_drop = ['ipAddress', 'domain', 'isp', 'lastReportedAt']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Encode 'countryCode' if it exists
if 'countryCode' in df.columns:
    df['countryCode'] = encoder.transform(df['countryCode'])

# Save actual labels if they exist (for evaluation)
true_labels = df['is_malicious'] if 'is_malicious' in df.columns else None

# Drop target column for prediction
if 'is_malicious' in df.columns:
    df = df.drop(columns=['is_malicious'])

# Reorder to match training features
X = df.reindex(columns=feature_columns, fill_value=0)

# Predict
predictions = model.predict(X)

# Show predictions
df['prediction'] = predictions
print(df[['prediction']].head(10))  # Show first 10 predictions

# Optionally evaluate performance
if true_labels is not None:
    from sklearn.metrics import classification_report
    print("\nModel Evaluation on Given Data:")
    print(classification_report(true_labels, predictions))

# Save predictions to CSV
output_path = 'predictions_output.csv'
df.to_csv(output_path, index=False)
print(f"\nPredictions saved to {output_path}")

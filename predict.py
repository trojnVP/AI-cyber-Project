import pandas as pd
import joblib

# Load the saved model
model = joblib.load('models/random_forest_model.pkl')

# Define a sample input that matches the training features exactly
sample_data = {
    'countryCode': [85],
    'abuseConfidenceScore': [100],
    'report_hour': [14],
    'report_day': [1]
}

# Create DataFrame for prediction
sample = pd.DataFrame(sample_data)

# Predict
prediction = model.predict(sample)

# Map the prediction to the corresponding label
if prediction == 0:
    print("Prediction: Benign")
else:
    print("Prediction: Malicious")

# Additional prediction using the provided sample
sample = pd.DataFrame([[85, 70, 14, 3]], columns=['countryCode', 'abuseConfidenceScore', 'report_hour', 'report_day'])  # Adding columns to match training
prediction = model.predict(sample)

# Map the prediction to the corresponding label
if prediction == 0:
    print("Prediction: Benign")
else:
    print("Prediction: Malicious")

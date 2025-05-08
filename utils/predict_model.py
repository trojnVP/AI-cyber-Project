import joblib
import pandas as pd

# Load the trained model and feature column order
loaded_model = joblib.load('models/random_forest_model.pkl')
feature_columns = joblib.load('models/feature_columns.pkl')

# Example input — make sure it matches the *raw* structure of your training data
raw_data = pd.DataFrame([{
    'abuseConfidenceScore': 90,
    'countryCode': 'US',              # categorical
    'report_day': 3,
    'report_hour': 14
}])

# Encode or preprocess the data to match training-time processing
# For example: if 'countryCode' was one-hot encoded, you must do that here
# Here's a placeholder — update this block to match your training preprocessing logic

# Example label encoding (if used during training):
# from sklearn.preprocessing import LabelEncoder
# encoder = joblib.load('models/label_encoder_country.pkl')
# raw_data['countryCode'] = encoder.transform(raw_data['countryCode'])

# For this example, let's drop the categorical column (if you had done that during training)
raw_data = raw_data.drop(columns=['countryCode'])

# Reorder columns to match the training set
new_data = raw_data.reindex(columns=feature_columns, fill_value=0)

# Predict
predictions = loaded_model.predict(new_data)
print("Prediction:", predictions)

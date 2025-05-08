import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Load prepared data
df = pd.read_csv('data/prepared_data.csv')

# Drop non-numeric and irrelevant columns
columns_to_drop = ['ipAddress', 'domain', 'isp', 'lastReportedAt']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Handle the categorical column 'countryCode' (encode it using LabelEncoder)
encoder = LabelEncoder()
df['countryCode'] = encoder.fit_transform(df['countryCode'])

# Save the encoder for later use in predictions
os.makedirs('models', exist_ok=True)
joblib.dump(encoder, 'models/label_encoder_country.pkl')  # Save the encoder

# Define features and target
X = df.drop(columns=['is_malicious'])
y = df['is_malicious']

# Save column order for future prediction
feature_columns = X.columns.tolist()

# Print final columns used for model training
print("Training features:", feature_columns)

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model and feature columns
joblib.dump(model, 'models/random_forest_model.pkl')
joblib.dump(feature_columns, 'models/feature_columns.pkl')
print("\nModel and feature columns saved successfully to 'models/' directory.")

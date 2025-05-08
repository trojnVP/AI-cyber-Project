import pandas as pd
from sklearn.preprocessing import LabelEncoder

def prepare_data():
    # Read the cleaned data
    df = pd.read_csv('data/cleaned_data.csv')  # Adjusted the file path to be relative

    # Convert 'lastReportedAt' to datetime, and handle invalid or missing values
    df['lastReportedAt'] = pd.to_datetime(df['lastReportedAt'], errors='coerce', utc=True)
    
    # Handle any rows where 'lastReportedAt' could not be converted (e.g., NaT values)
    df = df.dropna(subset=['lastReportedAt'])  # Drop rows with invalid 'lastReportedAt' values

    # Extract useful time-related features
    df['report_hour'] = df['lastReportedAt'].dt.hour
    df['report_day'] = df['lastReportedAt'].dt.dayofweek  # Extract day of the week

    # Encode country codes
    label_encoder = LabelEncoder()
    df['countryCode'] = label_encoder.fit_transform(df['countryCode'])

    # Create a target column 'is_malicious' based on some criteria (you can modify the logic here)
    # For example: IPs from certain countries could be considered malicious, you can adjust as needed
    suspicious_countries = ['CN', 'RU', 'PK']  # Example: China, Russia, and Pakistan as suspicious
    df['is_malicious'] = df['countryCode'].apply(lambda x: 1 if label_encoder.inverse_transform([x])[0] in suspicious_countries else 0)

    # Save the prepared data
    df.to_csv('data/prepared_data.csv', index=False)  # Saving the file in the 'data' folder

    print("✅ Data preparation complete. Prepared data saved to data/prepared_data.csv")

# Run the data preparation function
if __name__ == "__main__":
    prepare_data()

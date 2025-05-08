import pandas as pd

# Load cleaned data
df = pd.read_csv('C:/Users/admin/Desktop/cyber project final/data/cleaned_data.csv')

# List of risky country codes (add more if needed)
risky_countries = ['PK']

# Rule 1: Duplicate IPs
duplicate_ips = df[df.duplicated('ipAddress', keep=False)]

# Rule 2: IPs from risky countries
risky_country_ips = df[df['countryCode'].isin(risky_countries)]

# Combine both
suspicious_ips = pd.concat([duplicate_ips, risky_country_ips]).drop_duplicates()

# Count occurrences
ip_counts = suspicious_ips['ipAddress'].value_counts().reset_index()
ip_counts.columns = ['ipAddress', 'count']

# Save alerts
ip_counts.to_csv('C:/Users/admin/Desktop/cyber project final/data/alerts.csv', index=False)

print("🚨 Analysis complete. Suspicious IPs saved to C:/Users/admin/Desktop/cyber project final/data/alerts.csv")

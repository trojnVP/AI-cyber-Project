import pandas as pd

# Load the raw data (updated path to the correct location)
df = pd.read_csv(r'C:\Users\admin\Desktop\cyber project final\data\ip_blacklist.csv')

# Simple preprocessing: remove duplicates and NaNs
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Save cleaned data (save to the same directory)
df.to_csv(r'C:\Users\admin\Desktop\cyber project final\data\cleaned_data.csv', index=False)

print("✅ Preprocessing complete. Cleaned data saved to C:/Users/admin/Desktop/cyber project final/data/cleaned_data.csv")

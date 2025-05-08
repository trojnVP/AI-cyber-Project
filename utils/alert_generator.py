import pandas as pd

# Load the suspicious IPs detected during analysis
try:
    df = pd.read_csv(r'C:\Users\admin\Desktop\cyber project final\data\alerts.csv')
except FileNotFoundError:
    print("❌ alerts.csv not found. Please run analyze.py first to generate this file.")
    exit()

if df.empty:
    print("✅ No suspicious IPs detected. alerts.csv is empty.")
else:
    print("🚨 Suspicious IPs Detected:")
    for index, row in df.iterrows():
        print(f"➡️  ALERT: IP Address {row['ipAddress']} appeared {row['count']} times")

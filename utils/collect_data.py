import requests
import pandas as pd
import os

API_KEY = "409d71fd1e0feff66f242785c971e23098047f82cf7de4d640e24e1bd0a874390a98cdeb8c569060"
URL = "https://api.abuseipdb.com/api/v2/blacklist"

HEADERS = {
    "Accept": "application/json",
    "Key": API_KEY
}

def fetch_blacklist():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()["data"]
        df = pd.DataFrame(data)
        # Ensure the directory exists
        os.makedirs(r"C:\Users\admin\Desktop\cyber project final\data", exist_ok=True)
        # Save to the correct path
        df.to_csv(r"C:\Users\admin\Desktop\cyber project final\data\ip_blacklist.csv", index=False)
        print(f"Fetched {len(df)} blacklisted IPs.")
    else:
        print("Failed to fetch data:", response.status_code, response.text)

if __name__ == "__main__":
    fetch_blacklist()


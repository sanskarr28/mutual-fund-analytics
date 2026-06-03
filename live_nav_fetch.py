import requests
import pandas as pd
import os

def fetch_and_save_nav(scheme_code, scheme_name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching data for {scheme_name} (Code: {scheme_code})...")
    
    # Send GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # The API returns 'meta' and 'data'. The NAV history is inside 'data'
        if 'data' in data and len(data['data']) > 0:
            df = pd.DataFrame(data['data'])
            
            # Save to raw folder
            filename = os.path.join('data', 'raw', f"nav_{scheme_code}.csv")
            df.to_csv(filename, index=False)
            print(f"Success! Saved {len(df)} records to {filename}\n")
        else:
            print(f"No NAV data found for {scheme_name}.\n")
    else:
        print(f"Failed to fetch {scheme_name}. Status code: {response.status_code}\n")

def main():
    # Dictionary of scheme codes and names from your Task 4 & 5 list
    schemes = {
        125497: "HDFC Top 100",     # Task 4
        119551: "SBI Bluechip",     # Task 5
        120503: "ICICI Bluechip",   # Task 5
        118632: "Nippon Large Cap", # Task 5
        119092: "Axis Bluechip",    # Task 5
        120841: "Kotak Bluechip"    # Task 5
    }
    
    for code, name in schemes.items():
        fetch_and_save_nav(code, name)

if __name__ == "__main__":
    main()
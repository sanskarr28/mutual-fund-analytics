import pandas as pd
import glob
import os

def inspect_datasets():
    # Look for all CSV files inside the data/raw folder
    raw_data_path = os.path.join('data', 'raw', '*.csv')
    csv_files = glob.glob(raw_data_path)
    
    if not csv_files:
        print("No CSV files found in data/raw/. Please check your folder structure!")
        return

    print(f"Found {len(csv_files)} datasets. Starting inspection...\n")

    for file in csv_files:
        file_name = os.path.basename(file)
        print(f"{'='*60}")
        print(f"FILE: {file_name}")
        print(f"{'='*60}")
        
        try:
            df = pd.read_csv(file)
            print(f"SHAPE: {df.shape[0]} rows, {df.shape[1]} columns\n")
            print("DATA TYPES:")
            print(df.dtypes, "\n")
            print("FIRST 5 ROWS:")
            print(df.head())
            print("\n")
        except Exception as e:
            print(f"Error reading {file_name}: {e}\n")

if __name__ == "__main__":
    inspect_datasets()
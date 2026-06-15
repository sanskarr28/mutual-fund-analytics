import pandas as pd
import sys
from pathlib import Path

def inspect_datasets(raw_data_dir: str = "data/raw") -> None:
    """
    Inspects all CSV files in the specified directory, printing their shape,
    data types, missing values, and a preview of the data.
    """
    # Use pathlib for robust, cross-platform path handling
    data_path = Path(raw_data_dir)
    csv_files = list(data_path.glob('*.csv'))
    
    if not csv_files:
        print(f"⚠️ No CSV files found in '{data_path.resolve()}'. Please check your folder structure!")
        return

    print(f"🔍 Found {len(csv_files)} dataset(s). Starting inspection...\n")

    for file_path in csv_files:
        print(f"{'='*60}")
        print(f"📄 FILE: {file_path.name}")
        print(f"{'='*60}")
        
        try:
            # Read the dataset
            df = pd.read_csv(file_path)
            
            # 1. Shape
            print(f"📐 SHAPE: {df.shape[0]} rows, {df.shape[1]} columns\n")
            
            # 2. Data Types & Missing Values
            print("⚙️ DATA TYPES & MISSING VALUES:")
            info_df = pd.DataFrame({
                'Data Type': df.dtypes,
                'Missing Values': df.isnull().sum(),
                '% Missing': (df.isnull().sum() / len(df) * 100).round(2)
            })
            print(info_df.to_string())
            print("\n")
            
            # 3. Preview
            print("👀 FIRST 5 ROWS:")
            print(df.head().to_string())
            print("\n")
            
        except pd.errors.EmptyDataError:
            print(f"❌ Error: {file_path.name} is empty.\n")
        except Exception as e:
            print(f"❌ Error reading {file_path.name}: {e}\n")

if __name__ == "__main__":
    # Check if pandas is properly installed before running
    if 'pandas' not in sys.modules:
        print("Pandas is not installed. Please install it using 'pip install pandas'.")
        sys.exit(1)
        
    inspect_datasets()
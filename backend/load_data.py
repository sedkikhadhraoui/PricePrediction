# load_data.py

import pandas as pd

def load_csv():
    """
    Loads 'orders.csv' from the backend folder inside the project folder in Documents.
    """
    file_path = r"C:\Users\sedki\Documents\project\backend\orders.csv"
    
    try:
        df = pd.read_csv(file_path)
        print(f"✅ CSV file loaded successfully. Dimensions: {df.shape}")
        return df
    except FileNotFoundError:
        print("❌ File not found. Please confirm the file exists at:")
        print(file_path)
    except pd.errors.ParserError:
        print("❌ Format error. Make sure it's a valid CSV file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    data = load_csv()
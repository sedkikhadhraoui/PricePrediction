# clean_data.py

import pandas as pd
from load_data import load_csv

def clean_data(df):
    """
    Cleans the dataset by:
    - Dropping irrelevant columns
    - Removing rows with missing values
    """
    columns_to_drop = [
        'order_id', 'order_num', 'expected_date', 'reception_date', 'delivery_date',
        'qty_min', 'qty_max', 'qty_produced', 'qty_delivered',
        'order_status', 'part_id', 'isbn13', 'title',
        'part_status', 'security_label', 'siren'
    ]
    
    # Drop irrelevant columns if they exist
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors='ignore')
    
    # Remove rows with missing values
    df = df.dropna()

    print(f"✅ Data cleaned successfully. Shape after cleaning: {df.shape}")
    return df

# Example usage
if __name__ == "__main__":
    raw_data = load_csv()               # Load CSV from previous script
    cleaned_data = clean_data(raw_data) # Clean the data
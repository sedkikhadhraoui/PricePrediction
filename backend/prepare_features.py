# prepare_features.py

import pandas as pd
from clean_data import clean_data
from load_data import load_csv

def prepare_features(df):
    """
    Prepares X (features) and y (target) from the cleaned dataset.
    Performs one-hot encoding on categorical columns.
    """
    # Target variable
    y = df['unit_price']

    # Drop target from features
    X = df.drop('unit_price', axis=1)

    # List of categorical columns to encode
    categorical_cols = ['binding_type', 'priority_level',
                        'text_paper_type', 'cover_finish_type', 'text_color']

    # One-hot encode categorical columns
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

    print(f"✅ Features prepared. Shape of X: {X.shape}, Shape of y: {y.shape}")
    return X, y

# Example usage
if __name__ == "__main__":
    df = clean_data(load_csv())
    X, y = prepare_features(df)
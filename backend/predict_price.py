# predict_price.py

import pandas as pd
import joblib
from prepare_features import prepare_features
from clean_data import clean_data
from load_data import load_csv

def preprocess_new_data(new_data, reference_df):
    """
    Preprocesses a new order dict using the same structure as training data.
    Applies one-hot encoding using reference columns.
    """
    new_df = pd.DataFrame([new_data])
    
    # Get reference columns from training feature preparation
    reference_X, _ = prepare_features(reference_df)

    # Encode categorical features
    categorical_cols = ['binding_type', 'priority_level',
                        'text_paper_type', 'cover_finish_type', 'text_color']
    new_df = pd.get_dummies(new_df, columns=categorical_cols, drop_first=True)

    # Align columns with training set
    new_df = new_df.reindex(columns=reference_X.columns, fill_value=0)

    return new_df

def predict_new_price(new_data):
    """
    Predicts unit price for a new order input.
    """
    # Load trained model
    model = joblib.load("price_predictor_model.pkl")

    # Load reference data for feature structure
    reference_df = clean_data(load_csv())

    # Preprocess new input
    processed_input = preprocess_new_data(new_data, reference_df)

    # Make prediction
    predicted_price = model.predict(processed_input)[0]
    print(f"💰 Predicted unit price: {predicted_price:.2f}")
    return predicted_price

# Example usage
if __name__ == "__main__":
    example_order = {
        "quantity": 500,
        "priority_level": "NORMAL",
        "binding_type": "COILHARD-TAB",
        "shrinkwrap": 1,
        "three_hole_drill": 0,
        "perf": 0,
        "production_page": 588,
        "thickness": 21.4,
        "height": 306.38,
        "width": 254.0,
        "weight": 1660.59,
        "text_paper_type": "FSC_MC_CVG_SilkHO_1.0_70",
        "cover_finish_type": "LAYFLAT-GLOSS",
        "text_color": "4/4"
    }
    
    predict_new_price(example_order)
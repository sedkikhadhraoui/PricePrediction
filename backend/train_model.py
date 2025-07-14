# train_model.py

import pandas as pd
from prepare_features import prepare_features
from clean_data import clean_data
from load_data import load_csv
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def train_model(X, y):
    """
    Trains an XGBoost regression model and evaluates its performance.
    """
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"✅ Model trained successfully.")
    print(f"📉 Mean Squared Error: {mse:.2f}")
    print(f"📈 R² Score: {r2:.2f}")

    # Save the model
    joblib.dump(model, 'price_predictor_model.pkl')
    print("💾 Model saved as 'price_predictor_model.pkl'.")

    return model

# Example usage
if __name__ == "__main__":
    df = clean_data(load_csv())
    X, y = prepare_features(df)
    trained_model = train_model(X, y)
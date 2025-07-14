# app.py

from flask import Flask, request, jsonify ,render_template
import joblib
import pandas as pd
from prepare_features import prepare_features
from clean_data import clean_data
from load_data import load_csv
from predict_price import preprocess_new_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# Load the trained model once
model = joblib.load("price_predictor_model.pkl")
reference_df = clean_data(load_csv())

from flask import render_template

@app.route("/")
def homepage():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        input_df = preprocess_new_data(data, reference_df)
        prediction = model.predict(input_df)[0]
        return jsonify({'predicted_unit_price': float(round(prediction, 2))})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
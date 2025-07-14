# test_prediction.py

import requests

# URL of your local Flask API
url = "http://localhost:5000/predict"

# Sample order data (you can modify this anytime)
order_data = {
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

# Make the POST request
response = requests.post(url, json=order_data)

# Show the result
if response.ok:
    print(f"✅ Predicted price: {response.json()['predicted_unit_price']:.2f}")
else:
    print(f"❌ Error: {response.text}")
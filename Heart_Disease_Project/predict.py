import pickle
from flask import Flask, request, jsonify
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
model_path = script_dir / 'model.bin'

# Load the model
with open(model_path, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('heart_disease')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict heart disease probability
    
    Expected JSON input:
    {
        "age": 52,
        "sex": 1,
        "cp": 0,
        "trestbps": 125,
        "chol": 212,
        "fbs": 0,
        "restecg": 1,
        "thalach": 168,
        "exang": 0,
        "oldpeak": 1.0,
        "slope": 2,
        "ca": 2,
        "thal": 3
    }
    """
    patient = request.get_json()
    
    # Transform input
    X = dv.transform([patient])
    
    # Make prediction
    y_pred = model.predict_proba(X)[0, 1]
    heart_disease = y_pred >= 0.5
    
    result = {
        'heart_disease_probability': float(y_pred),
        'heart_disease': bool(heart_disease)
    }
    
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model': 'loaded'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
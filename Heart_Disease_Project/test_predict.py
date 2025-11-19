import requests

# URL of the Flask service
url = 'http://localhost:9696/predict'

# Example patient data - you can modify these values
patient_1 = {
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

# Another example - healthier patient
patient_2 = {
    "age": 45,
    "sex": 0,
    "cp": 0,
    "trestbps": 110,
    "chol": 180,
    "fbs": 0,
    "restecg": 0,
    "thalach": 175,
    "exang": 0,
    "oldpeak": 0.0,
    "slope": 1,
    "ca": 0,
    "thal": 2
}

# Test patient 1
print("Testing Patient 1:")
print("Input data:", patient_1)
response = requests.post(url, json=patient_1)
result = response.json()
print("Prediction:", result)
print(f"Heart Disease Probability: {result['heart_disease_probability']:.2%}")
print(f"Diagnosis: {'Heart Disease Detected' if result['heart_disease'] else 'No Heart Disease'}")
print("\n" + "="*60 + "\n")

# Test patient 2
print("Testing Patient 2:")
print("Input data:", patient_2)
response = requests.post(url, json=patient_2)
result = response.json()
print("Prediction:", result)
print(f"Heart Disease Probability: {result['heart_disease_probability']:.2%}")
print(f"Diagnosis: {'Heart Disease Detected' if result['heart_disease'] else 'No Heart Disease'}")
print("\n" + "="*60 + "\n")

# Test health endpoint
print("Testing Health Endpoint:")
health_response = requests.get('http://localhost:9696/health')
print("Health Status:", health_response.json())
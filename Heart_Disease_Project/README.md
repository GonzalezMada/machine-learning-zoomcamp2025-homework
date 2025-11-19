# Heart Disease Binary Classification (scikit-learn)

## Description

This project builds a binary classifier to predict the presence of heart disease from clinical features using the "heart disease dataset" available at:
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

### Why this problem matters
- Early detection of heart disease can guide clinical decisions and help prioritize patients for further tests.
- A classification model can estimate risk given routine clinical and lab features.
- The model can be used as a lightweight screening tool (not a substitute for clinical judgement).

## Dataset Features

The dataset includes the following features:
- **age**: Age in years
- **sex**: Sex (0 = female, 1 = male)
- **cp**: Chest pain type (0-3)
- **trestbps**: Resting blood pressure (mm Hg)
- **chol**: Serum cholesterol (mg/dl)
- **fbs**: Fasting blood sugar > 120 mg/dl (0 = false, 1 = true)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (0 = no, 1 = yes)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment (0-2)
- **ca**: Number of major vessels colored by fluoroscopy (0-4)
- **thal**: Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect, 3 = other)
- **target**: Presence of heart disease (0 = no, 1 = yes)

## Project Structure

```
Heart_Disease_Project/
├── data/
│   └── heart.csv           # Dataset
├── notebook.ipynb          # Exploratory analysis and model development
├── train.py                # Script to train and save the model
├── predict.py              # Flask web service for predictions
├── test_predict.py         # Test client script
├── model.bin               # Trained model (generated after running train.py)
└── README.md               # This file
```

## Installation

### Required Libraries

Install the required Python packages:

```bash
pip install pandas numpy scikit-learn matplotlib flask requests
```

Or using a requirements.txt file:

```bash
pip install -r requirements.txt
```

**requirements.txt content:**
```
pandas
numpy
scikit-learn
matplotlib
flask
requests
```

## Usage

### 1. Train the Model

First, train the model and save it to `model.bin`:

```bash
python train.py
```

Expected output:
```
AUC on test data: 0.921
Model saved to model.bin
```

### 2. Start the Prediction Service

Run the Flask web service:

```bash
python predict.py
```

The service will start on `http://localhost:9696`

Expected output:
```
 * Running on http://0.0.0.0:9696
 * Running on http://127.0.0.1:9696
```

**Note:** Keep this terminal running while making predictions!

### 3. Make Predictions

You have two options to test the prediction service:

#### Option 1: Using the Test Script (Recommended)

Open a **new terminal window** and run:

```bash
python test_predict.py
```

This will test two example patients and display their heart disease predictions.

The output that I have got:
```
Testing Patient 1:
Input data: {'age': 52, 'sex': 1, 'cp': 0, ...}
Prediction: {'heart_disease': False, 'heart_disease_probability': 0.2482}
Heart Disease Probability: 24.82%
Diagnosis: No Heart Disease

============================================================

Testing Patient 2:
Input data: {'age': 45, 'sex': 0, 'cp': 0, ...}
Prediction: { 'heart_disease': True, 'heart_disease_probability': 0.9491,}
Heart Disease Probability: 94.91%
Diagnosis: Heart Disease Detected
```

#### Option 2: Using curl

You can also make predictions using curl from the command line:

```bash
curl -X POST http://localhost:9696/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 60,
    "sex": 1,
    "cp": 0,
    "trestbps": 140,
    "chol": 293,
    "fbs": 0,
    "restecg": 1,
    "thalach": 170,
    "exang": 0,
    "oldpeak": 1.2,
    "slope": 1,
    "ca": 2,
    "thal": 3
  }'
```

Response that I have got:
```json
{
  "heart_disease": false,
  "heart_disease_probability": 0.09625
}
```

#### Option 3: Using Python Requests

You can also create your own Python script to make predictions:

```python
import requests

url = 'http://localhost:9696/predict'

patient = {
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

response = requests.post(url, json=patient)
result = response.json()
print(f"Heart Disease Probability: {result['heart_disease_probability']:.2%}")
print(f"Diagnosis: {'Detected' if result['heart_disease'] else 'Not Detected'}")
```

### GET /health
Check if the service is running.

**Response:**
```json
{
  "status": "healthy",
  "model": "loaded"
}
```

## Model Performance

The Logistic Regression model achieves:
- **AUC**: 0.921 on the test set
- **Accuracy**: 81.0%
- **Sensitivity/Recall**: 89.6%
- **Specificity**: 73.4%
- **Precision**: 74.8%

The model uses regularization parameter C=1.0, selected through cross-validation.

## Notes

- The model is trained on 1,025 samples with 14 features
- Logistic Regression was chosen for its interpretability and good performance
- The prediction threshold is set at 0.5 (can be adjusted based on use case)
- This is a demonstration project and should not be used for actual medical diagnosis

## License

This project is for educational purposes.
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold
	
import pickle

#Load the dataset
df = pd.read_csv('data/heart.csv')
# Split the dataset
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
# Reset indexes
df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
# Separate target variable
y_test = df_test.target.values
# Remove target from dataframes
del df_test['target']

#numerical and categorical variables
numerical = ['age', 'sex', 'trestbps', 'chol', 'thalach', 'oldpeak']
categorical = ['cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']


# Train the model
def train (df_train, y_train, C=1.0):
    train_dicts = df_train[categorical + numerical].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dicts)
    
    model = LogisticRegression(C=C, max_iter=len(X_train)*10)
    model.fit(X_train, y_train)
    
    return dv, model
dv, model = train(df_full_train, df_full_train.target.values, C=1)
y_pred = model.predict_proba(dv.transform(df_test[categorical + numerical].to_dict(orient='records')))[:, 1]
auc = roc_auc_score(y_test, y_pred)
print(f'AUC on test data: {auc:.3f}')

#Save the model
with open('model.bin', 'wb') as f_out:
    pickle.dump((dv, model), f_out)
print("Model saved to model.bin")

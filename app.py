from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# Load pre-trained model
model_path = "model.joblib"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None


# Input schema for prediction
class PredictionInput(BaseModel):
    Temperature: float
    Run_Time: float


# Endpoint to upload data
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    # Save the uploaded file
    data_path = "data/synthetic_manufacturing_data.csv"
    with open(data_path, "wb") as f:
        f.write(file.file.read())

    return {"message": "File uploaded successfully"}


# Endpoint to train the model
@app.post("/train")
async def train():
    data_path = "data/synthetic_manufacturing_data.csv"
    if not os.path.exists(data_path):
        raise HTTPException(status_code=400, detail="No uploaded data found. Use /upload first.")

    # Load data
    data = pd.read_csv(data_path)
    if "Temperature" not in data.columns or "Run_Time" not in data.columns or "Downtime_Flag" not in data.columns:
        raise HTTPException(status_code=400,
                            detail="Dataset must contain 'Temperature', 'Run_Time', and 'Downtime_Flag' columns.")

    # Features and target
    X = data[['Temperature', 'Run_Time']]
    y = data['Downtime_Flag']

    # Train a new model
    from sklearn.linear_model import LogisticRegression
    global model
    model = LogisticRegression()
    model.fit(X, y)

    # Save the model
    joblib.dump(model, model_path)
    return {"message": "Model trained successfully"}


# Endpoint to make predictions
@app.post("/predict")
async def predict(input: PredictionInput):
    if model is None:
        raise HTTPException(status_code=400, detail="Model not trained yet. Use /train first.")

    # Prepare input for prediction
    data = [[input.Temperature, input.Run_Time]]
    prediction = model.predict(data)
    confidence = model.predict_proba(data).max()

    return {
        "Downtime": "Yes" if prediction[0] == 1 else "No",
        "Confidence": round(confidence, 2)
    }


# Dynamically set the URL for the API call
url = "http://host.docker.internal:8000/predict" if os.getenv("DOCKER_ENV") else "http://localhost:8000/predict"

data = {"Temperature": 80, "Run_Time": 120}
try:
    response = requests.post(url, json=data)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")

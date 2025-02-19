from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.ml.model import PricePredictor
import pandas as pd

app = FastAPI(title="Price Tracker API")
model = PricePredictor()

# Initialize model with some training data
try:
    X_train = pd.DataFrame({
        'feature1': [1.0, 2.0, 3.0],
        'feature2': [2.0, 4.0, 6.0]
    })
    y_train = [100.0, 200.0, 300.0]
    model.train(X_train, y_train)
except Exception as e:
    print(f"Warning: Could not train model: {e}")

class PredictionRequest(BaseModel):
    feature1: float
    feature2: float

class PredictionResponse(BaseModel):
    prediction: float

@app.get("/")
def read_root():
    return {"message": "Price Tracker API"}

@app.post("/predict", response_model=PredictionResponse)
def predict_price(request: PredictionRequest):
    try:
        prediction = model.predict({
            "feature1": [request.feature1],
            "feature2": [request.feature2]
        })
        return PredictionResponse(prediction=float(prediction[0]))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
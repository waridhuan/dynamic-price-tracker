from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.ml.model import PricePredictor

app = FastAPI(title="Price Tracker API")
model = PricePredictor()


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
        prediction = model.predict(
            {"feature1": [request.feature1], "feature2": [request.feature2]}
        )
        return PredictionResponse(prediction=float(prediction[0]))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

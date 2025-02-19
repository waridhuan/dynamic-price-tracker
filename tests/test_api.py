import pytest
from fastapi.testclient import TestClient
from src.api.main import app, model
import pandas as pd

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Price Tracker API"}

def test_predict_price():
    # Train the model first
    X_train = pd.DataFrame({
        'feature1': [1.0, 2.0, 3.0],
        'feature2': [2.0, 4.0, 6.0]
    })
    y_train = [100.0, 200.0, 300.0]
    model.train(X_train, y_train)
    
    # Test prediction endpoint
    test_data = {
        "feature1": 2.0,
        "feature2": 4.0
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], float)

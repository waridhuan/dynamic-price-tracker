import pytest
from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Price Tracker API"}


def test_predict_price():
    test_data = {"feature1": 1.0, "feature2": 2.0}
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "prediction" in response.json()

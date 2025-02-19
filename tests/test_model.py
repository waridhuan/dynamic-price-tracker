import pytest

from src.ml.model import PricePredictor


def test_model_initialization():
    model = PricePredictor()
    assert model is not None


def test_model_prediction():
    model = PricePredictor()
    # Add sample test data
    sample_data = {"feature1": [1.0], "feature2": [2.0]}
    prediction = model.predict(sample_data)
    assert prediction is not None

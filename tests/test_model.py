import pytest
import pandas as pd
from src.ml.model import PricePredictor

def test_model_initialization():
    model = PricePredictor()
    assert model is not None

def test_model_prediction():
    model = PricePredictor()
    
    # Create sample training data
    X_train = pd.DataFrame({
        'feature1': [1.0, 2.0, 3.0],
        'feature2': [2.0, 4.0, 6.0]
    })
    y_train = [100.0, 200.0, 300.0]
    
    # Train the model first
    model.train(X_train, y_train)
    
    # Test prediction
    sample_data = {
        'feature1': [2.0],
        'feature2': [4.0]
    }
    prediction = model.predict(sample_data)
    assert prediction is not None
    assert isinstance(prediction[0], float)

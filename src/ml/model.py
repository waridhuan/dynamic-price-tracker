import pandas as pd
from sklearn.ensemble import RandomForestRegressor


class PricePredictor:
    def __init__(self):
        self.model = RandomForestRegressor()
        self.is_trained = False

    def train(self, X, y):
        """Train the model with given features and target"""
        self.model.fit(X, y)
        self.is_trained = True

    def predict(self, features):
        """Make price predictions"""
        if not self.is_trained:
            raise ValueError("Model needs to be trained first")

        # Convert input to DataFrame if it's a dict
        if isinstance(features, dict):
            features = pd.DataFrame(features)

        return self.model.predict(features)

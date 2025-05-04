# inference.py
import joblib
from sklearn.base import BaseEstimator

_model: BaseEstimator | None = None


def load_model(filename="model.joblib"):
    global _model
    if _model is None:
        _model = joblib.load(filename)
    return _model


def predict(sepal_length, sepal_width, petal_length, petal_width):
    model = load_model()
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    pred = model.predict(input_data)[0]
    return str(pred)

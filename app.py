from fastapi import FastAPI
from inference import load_model, predict as predict_class
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "api")))
from api.models.iris import PredictRequest, PredictResponse


app = FastAPI()

model = load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    # Extract features and make prediction
    prediction = predict_class(
        sepal_length=request.sepal_length,
        sepal_width=request.sepal_width,
        petal_length=request.petal_length,
        petal_width=request.petal_width,
    )
    return PredictResponse(prediction=prediction)

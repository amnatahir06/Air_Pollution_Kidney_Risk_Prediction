from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

app = FastAPI()

# allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model
model = joblib.load("kidney_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")


@app.get("/")
def home():
    return {"message": "Kidney Risk Prediction API running"}


@app.post("/predict")
def predict(data: dict):

    # model input (same order as training)
    input_data = np.array([[
        data["age"],
        data["gender"],
        data["systolic_bp"],
        data["diastolic_bp"],
        data["urine_creatinine"],
        data["urine_albumin"]
    ]])

    pred = model.predict(input_data)[0]
    risk = label_encoder.inverse_transform([pred])[0]

    # recommendations
    recommendations = []

    if risk == "High":
        recommendations = [
            "Consult a nephrologist immediately.",
            "Avoid outdoor activity during high pollution hours.",
            "Monitor blood pressure regularly.",
            "Reduce salt intake and stay hydrated."
        ]
    elif risk == "Medium":
        recommendations = [
            "Regular kidney checkups advised.",
            "Maintain healthy blood pressure.",
            "Avoid prolonged exposure to polluted environments."
        ]
    else:
        recommendations = [
            "Maintain a healthy lifestyle.",
            "Regular exercise and hydration recommended."
        ]

    return {
        "risk_level": risk,
        "recommendations": recommendations
    }

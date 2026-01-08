# Air_Pollution_Kidney_Risk_Prediction
### 🩺 Kidney Risk Prediction System

End-to-End Machine Learning Project

An end-to-end Machine Learning–based Kidney Risk Prediction System that analyzes real-world health indicators to predict kidney risk levels and provide personalized recommendations and precautions.
The project demonstrates the complete Data Science lifecycle: data understanding, preprocessing, model training, API development, and frontend integration.

### Project Motivation

Chronic Kidney Disease (CKD) is a serious global health issue that often remains undetected until advanced stages. Early identification of kidney risk can significantly improve patient outcomes through timely medical intervention and lifestyle changes.

This project aims to:

Leverage machine learning for early kidney risk prediction

Use real-world health parameters

Provide actionable recommendations rather than only predictions

Demonstrate a production-ready ML pipeline

### Key Objectives

Build a machine learning model to classify kidney risk levels

Develop a REST API for real-time predictions

Create a user-friendly frontend for data input

Provide risk-based health recommendations and precautions

Design a future-ready system suitable for wearable device integration

### Machine Learning Overview

Problem Type: Multi-class Classification

Algorithm Used: Random Forest Classifier

Target Variable: Kidney Risk Level (Low / Medium / High)

### Input Features

Age

Gender

Systolic Blood Pressure

Diastolic Blood Pressure

Urine Creatinine

Urine Albumin

### Model Evaluation

Train-test split

Accuracy-based evaluation

Overfitting checks and validation

### Technology Stack

Programming Language: Python

Data Analysis: Pandas, NumPy

Machine Learning: Scikit-learn

Backend API: FastAPI

Frontend: HTML, CSS, JavaScript

Model Serialization: Joblib

Version Control: Git & GitHub

### 📂 Project Structure
```
Air_Pollution_Kidney_Risk_Project/
│
├── app.py                     # FastAPI backend
├── kidney_model.pkl           # Trained ML model
├── label_encoder.pkl          # Label encoder
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
│
├── frontend/
│   ├── index.html             # Frontend UI
│   └── image.jpg              # Background image
│
└── data/
    └── real-world datasets    # NHANES & health-related datasets
```

### How to Run the Project
1️⃣ Backend Setup (FastAPI)
pip install -r requirements.txt
python -m uvicorn app:app --reload


Backend will run at:

http://127.0.0.1:8000

2️⃣ Frontend Setup
cd frontend
python -m http.server 5500


Open in browser:

http://127.0.0.1:5500/index.html

### System Output

The system provides:

Predicted Kidney Risk Level

Personalized Health Recommendations

Risk-Level–Based Precautions

This ensures that users receive actionable insights, not just predictions.

### Future Enhancements

Integration with wearable devices (smartwatches, fitness bands)

Real-time health data ingestion (heart rate, activity level, BP)

Mobile application development

Cloud deployment for scalability

Explainable AI (XAI) for medical transparency

### Disclaimer

This project is intended for educational and research purposes only.
It does not replace professional medical diagnosis or treatment.

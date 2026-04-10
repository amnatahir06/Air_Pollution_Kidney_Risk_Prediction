<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/NHANES-Data-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

# 🩺 Air Pollution & Kidney Risk Prediction System

An end-to-end Machine Learning web application that predicts **kidney disease risk levels** (Low / Medium / High) based on clinical health parameters sourced from real-world **NHANES (National Health and Nutrition Examination Survey)** data, with a focus on the relationship between air pollution exposure and kidney health.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Model Details](#-model-details)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

Chronic kidney disease (CKD) is a growing global health concern, and exposure to air pollution has been identified as a contributing risk factor. This project builds a **predictive system** that:

1. **Ingests** real clinical data from NHANES (demographics, blood pressure, kidney biomarkers).
2. **Trains** a Random Forest classifier to categorize patients into risk tiers.
3. **Serves** predictions via a FastAPI REST backend.
4. **Presents** an intuitive web-based frontend for healthcare professionals and patients.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Real-World Data** | Built on NHANES SAS transport files — demographics, blood pressure, albumin/creatinine ratios |
| **ML Prediction** | Random Forest model with 200 estimators and max depth of 10 for robust classification |
| **REST API** | FastAPI backend with `/predict` endpoint returning risk level, recommendations & precautions |
| **Web Frontend** | Multi-page HTML interface with splash screen, login, dashboard, prediction form & health reference |
| **Risk-Aware Responses** | Tailored medical recommendations and precautions for each risk level |
| **Health Reference Guide** | Normal parameter values page for patient education |

---

## 🏗 Architecture

```
┌─────────────┐       HTTP/JSON       ┌──────────────────┐
│   Frontend   │ ──────────────────▶  │   FastAPI Server  │
│  (HTML/CSS/  │ ◀──────────────────  │   (app.py)        │
│   JS)        │     Prediction +     │                   │
└─────────────┘   Recommendations     │  ┌──────────────┐ │
                                      │  │ Random Forest│ │
                                      │  │   Model      │ │
                                      │  │ (.pkl files) │ │
                                      │  └──────────────┘ │
                                      └──────────────────┘
                                              ▲
                                              │ Training
                                     ┌────────┴────────┐
                                     │  Jupyter Notebook │
                                     │  (NHANES Data     │
                                     │   Processing)     │
                                     └──────────────────┘
```

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **ML Framework** | Scikit-learn (Random Forest Classifier) |
| **Backend** | FastAPI + Uvicorn |
| **Data Processing** | Pandas, NumPy |
| **Model Serialization** | Joblib |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Data Source** | NHANES (CDC) — SAS Transport (.xpt) files |

---

## 📊 Dataset

### Source
Data comes from the **CDC NHANES 2017–2018** survey cycle:

| File | Description | Key Variables |
|---|---|---|
| `DEMO_J.xpt` | Demographics | Age (`RIDAGEYR`), Gender (`RIAGENDR`) |
| `BPX_J.xpt` | Blood Pressure | Systolic (`BPXSY1`), Diastolic (`BPXDI1`) |
| `ALB_CR_J.xpt` | Albumin & Creatinine | Urine Albumin (`URXUMA`), Urine Creatinine (`URXUCR`) |
| `annual_aqi_by_county_2018.csv` | EPA Air Quality Index | County-level AQI data |

### Risk Labeling Criteria

| Risk Level | Condition |
|---|---|
| **High** | Albumin > 30 mg/g **OR** Creatinine > 150 mg/dL |
| **Medium** | Creatinine > 100 mg/dL |
| **Low** | Otherwise |

---

## 🤖 Model Details

| Parameter | Value |
|---|---|
| **Algorithm** | Random Forest Classifier |
| **Number of Estimators** | 200 |
| **Max Depth** | 10 |
| **Train/Test Split** | 80 / 20 (stratified) |
| **Input Features** | Age, Gender, Systolic BP, Diastolic BP, Urine Creatinine, Urine Albumin |
| **Output** | 3-class risk: Low, Medium, High |
| **Serialization** | `kidney_model.pkl`, `label_encoder.pkl` |

---

## 📁 Project Structure

```
Air_Pollution_Kidney_Risk_Project/
│
├── app.py                          # FastAPI backend server
├── requirements.txt                # Python dependencies
├── kidney_dataset.csv              # Processed training dataset
├── 2_data_loading_real.ipynb       # Data ingestion, EDA & model training notebook
│
├── data/                           # Raw NHANES data files
│   ├── DEMO_J.xpt                  # Demographics
│   ├── BPX_J.xpt                   # Blood pressure
│   ├── ALB_CR_J.xpt                # Albumin & Creatinine
│   ├── SMQ_J.xpt                   # Smoking questionnaire
│   └── annual_aqi_by_county_2018.csv  # EPA air quality data
│
└── frontend/                       # Web interface
    ├── splash.html                 # Loading screen
    ├── login.html                  # Authentication page
    ├── home.html                   # Dashboard / landing page
    ├── index.html                  # Prediction form
    └── manual.html                 # Normal health parameters reference
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Air_Pollution_Kidney_Risk_Project.git
cd Air_Pollution_Kidney_Risk_Project

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Train the Model (Optional)

If you want to retrain the model from raw NHANES data:

```bash
jupyter notebook 2_data_loading_real.ipynb
```

Run all cells to generate `kidney_model.pkl` and `label_encoder.pkl`.

### Run the Application

```bash
# Start the FastAPI backend
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

Then open `frontend/splash.html` in your browser (or serve it via a local HTTP server).

> **Demo Credentials:** `amna.mirza782@gmail.com` / `123456`

---

## 📡 API Reference

### `GET /`

Health check endpoint.

**Response:**
```json
{
  "message": "Kidney Risk Prediction API running"
}
```

### `POST /predict`

Predict kidney risk based on clinical inputs.

**Request Body:**
```json
{
  "age": 55,
  "gender": 1,
  "systolic_bp": 130,
  "diastolic_bp": 85,
  "urine_creatinine": 160,
  "urine_albumin": 35
}
```

| Field | Type | Description |
|---|---|---|
| `age` | float | Patient age in years |
| `gender` | float | 1 = Male, 0 = Female |
| `systolic_bp` | float | Systolic blood pressure (mmHg) |
| `diastolic_bp` | float | Diastolic blood pressure (mmHg) |
| `urine_creatinine` | float | Urine creatinine (mg/dL) |
| `urine_albumin` | float | Urine albumin (mg/g) |

**Response:**
```json
{
  "risk_level": "High",
  "recommendations": [
    "Consult a nephrologist immediately.",
    "Avoid outdoor activity during high pollution hours.",
    "Monitor blood pressure regularly.",
    "Reduce salt intake and stay hydrated."
  ],
  "precautions": [
    "Wear a mask in polluted environments",
    "Avoid smoking",
    "Drink at least 2–3 liters of water daily",
    "Limit processed food intake"
  ]
}
```

---

## 🖼 Screenshots

> _Add screenshots of the login page, dashboard, and prediction results here._

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **CDC NHANES** for providing open-access clinical survey data
- **EPA AQI** for county-level air quality datasets
- **Scikit-learn** & **FastAPI** open-source communities

---

<p align="center">
  Made with ❤️ for public health and data science
</p>

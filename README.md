# 🚑 AI Emergency Pressure & Ambulance Load Prediction System

## 📌 Project Title
**AI Emergency Pressure & Ambulance Load Prediction System**
## 👩‍💻 Author

**Deepika K**  
B.Tech Student | Aspiring Software Engineer  

GitHub: https://github.com/kamsalideepika  
LinkedIn: https://www.linkedin.com/in/deepikakamsali/

---

## 📖 Project Description

The **AI Emergency Pressure & Ambulance Load Prediction System** is an AI-driven healthcare support platform designed to assist hospitals and emergency response authorities in predicting sudden Emergency Department (ED) overload situations.

In real-world emergency scenarios, hospitals often face unexpected surges due to:

- Road accidents  
- Seasonal disease outbreaks  
- Festival or public event emergencies  
- Weather-related incidents  
- High ambulance arrival density  

This system helps reduce emergency chaos by providing early predictions and insights so that hospitals can prepare resources in advance.

---

## 🎯 Problem Statement

Hospitals and emergency services frequently struggle with:

- Sudden overload of emergency patients  
- Ambulance congestion at specific hospitals  
- Lack of early warning systems  
- Poor allocation of staff and beds during peak emergencies  
- No clear identification of accident hotspot zones  

This project aims to solve these challenges by building a prediction-based emergency readiness system.

---

## ✅ Phase 1: Core Implementation & Foundation

Phase 1 focuses on building the **backend foundation** and a working Minimum Viable Product (MVP).

The main goal of Phase 1 is:

- To establish a clean project architecture  
- Implement the primary entities (data models)  
- Setup database connectivity  
- Build basic working APIs for prediction and hotspot detection  
- Ensure the system is ready for AI/ML integration in later phases  

---

## 🚀 Phase 1 Objectives Achieved

In this phase, the following components were successfully implemented:

### ✅ Project Setup & Architecture
- FastAPI-based backend server created  
- Modular folder structure followed (`models`, `routes`, `services`)  
- Clean separation of logic for scalability  

### ✅ Database Foundation
- SQLAlchemy ORM setup  
- SQLite database used for MVP  
- Base connection and session handling included  

### ✅ Core Data Models Implemented
Primary entities required for emergency prediction:

- Hospital Model  
- Accident Record Model  
- Ambulance Arrival Log Model  

### ✅ MVP Features Built

#### 1. Emergency Pressure Prediction API
A basic endpoint that predicts emergency pressure levels based on:

- Accident count  
- Ambulance arrival load  

#### 2. Accident Hotspot Identification API
A basic endpoint that returns accident-prone zones using sample logic.

---

## 🏗️ Project Folder Structure

ai-emergency-system/
│
├── app/
│ ├── main.py
│ ├── database.py
│
│ ├── models/
│ │ ├── hospital.py
│ │ ├── accident.py
│ │ └── ambulance_log.py
│
│ ├── routes/
│ │ ├── prediction_routes.py
│ │ └── hotspot_routes.py
│
│ ├── services/
│ │ ├── pressure_service.py
│ │ └── hotspot_service.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Technologies Used

The following technologies were used in Phase 1:

- **Python 3**
- **FastAPI** – Web framework for building APIs
- **Uvicorn** – ASGI server for running FastAPI
- **SQLAlchemy** – ORM for database modeling
- **SQLite** – Lightweight database for MVP development

---

## 🛠️ Setup Instructions (Local Installation)

Follow these steps to run the Phase 1 MVP project locally.

---
## 🛠️ Setup Instructions (Local Installation)



## Follow these steps to run the Phase 1 MVP project locally.


```bash
1️⃣ Clone the Repository

git clone https://github.com/kamsalideepika/ai-emergency-system.git

cd ai-emergency-system

2️⃣ Create a Virtual Environment

A virtual environment helps keep project dependencies isolated.

Run the following command inside your project folder:

python -m venv venv

3️⃣ Activate the Virtual Environment

Activate the environment before installing dependencies.

For Windows PowerShell:

.\venv\Scripts\activate

After activation, your terminal will look like:

(venv) PS C:\Users\ganes\Downloads\ai-emergency-system>

4️⃣ Install Required Dependencies

Install all required Python libraries using:

pip install -r requirements.txt

This installs:

FastAPI

Uvicorn

SQLAlchemy

Pydantic

5️⃣ Run the FastAPI Server

Start the backend server using:

uvicorn app.main:app --reload

Expected output:

INFO: Uvicorn running on http://127.0.0.1:8000

INFO: Application startup complete.

6️⃣ Open the API Documentation

Once the server is running, open your browser and visit:

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc Documentation:

http://127.0.0.1:8000/redoc

7️⃣ Test the MVP Endpoints
Root Endpoint

GET /

Response:

{
"message": "Phase 1 MVP Running Successfully ✅"
}

Emergency Pressure Prediction

GET /predict-pressure?accidents=5&ambulance_load=3

Response:

{
"accidents_reported": 5,
"ambulance_load": 3,
"predicted_pressure": "MODERATE ⚠️"
}

Accident Hotspot Detection

GET /hotspots

Response:

{
"message": "Accident Hotspot Zones Identified",
"hotspots": [
{
"zone": "Zone-A",
"accident_count": 3
},
{
"zone": "Zone-B",
"accident_count": 2
}
]
}
This repository contains the complete Phase 1 MVP implementation of the
AI Emergency Pressure & Ambulance Load Prediction System, developed as part of the project requirements.

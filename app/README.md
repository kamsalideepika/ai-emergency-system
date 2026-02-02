# 🚑 AI Emergency Pressure & Ambulance Load Prediction System

## Phase 1: Core Implementation & Foundation (MVP)

This project is an AI-driven emergency preparedness system designed to help hospitals and emergency authorities predict sudden Emergency Department (ED) overloads.

Phase 1 focuses on building the core foundation and minimum viable product (MVP).

---

## 🎯 Objective

The system aims to:

- Predict emergency pressure on hospitals
- Identify accident-prone hotspot zones
- Forecast ambulance arrival density
- Trigger early alerts for better emergency preparedness

---

## ✅ Phase 1 Features Implemented

### Core Entities (Data Models)

- **Hospital**
- **Accident**
- **Ambulance Arrival Logs**

### MVP Core Functionalities

- Emergency Pressure Prediction API  
- Accident Hotspot Zone Identification API  
- FastAPI-based backend architecture  
- Clean modular folder structure

---

## 🛠 Tech Stack

- Python
- FastAPI
- SQLite (Database)
- SQLAlchemy (ORM)
- Uvicorn (Server)

---

## 📂 Project Structure

ai-emergency-system/
│
├── app/
│ ├── main.py
│ ├── database.py
│ │
│ ├── models/
│ │ ├── hospital.py
│ │ ├── accident.py
│ │ ├── ambulance_log.py
│ │
│ ├── routes/
│ │ ├── prediction_routes.py
│ │ ├── hotspot_routes.py
│ │
│ ├── services/
│ │ ├── pressure_service.py
│ │ ├── hotspot_service.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```powershell
py -m venv venv
.\venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy pydantic

uvicorn app.main:app --reload

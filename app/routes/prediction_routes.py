from fastapi import APIRouter
from app.services.pressure_service import calculate_pressure

router = APIRouter()

@router.get("/predict-pressure")
def predict_pressure(accidents: int, ambulance_load: int):
    result = calculate_pressure(accidents, ambulance_load)

    return {
        "accidents_reported": accidents,
        "ambulance_load": ambulance_load,
        "predicted_pressure": result
    }

from fastapi import APIRouter, Query
from app.services.pressure_service import predict_emergency_pressure

router = APIRouter()

@router.get("/predict-pressure")
def predict_pressure(
    accidents: int = Query(..., ge=0),
    ambulance_load: int = Query(..., ge=0)
):
    """
    Predict emergency overload pressure.
    Includes validation + alert support.
    """

    if accidents > 500:
        return {"error": "Accident count too high for MVP limit"}

    return predict_emergency_pressure(accidents, ambulance_load)


from app.ml.pressure_forecast import forecast_pressure
from app.alerts.alert_engine import generate_alert

def predict_emergency_pressure(accidents: int, ambulance_load: int):

    # Forecast ED pressure
    level = forecast_pressure(accidents, ambulance_load)

    # Generate alert
    alert_message = generate_alert(level)

    return {
        "accidents_reported": accidents,
        "ambulance_load": ambulance_load,
        "predicted_pressure": level,
        "alert": alert_message
    }


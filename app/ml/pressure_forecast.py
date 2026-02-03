import datetime

def forecast_pressure(accidents: int, ambulance_load: int):
    """
    Time-series placeholder logic.
    Later replaced with ARIMA/LSTM.
    """

    hour = datetime.datetime.now().hour

    base_score = accidents * 2 + ambulance_load * 3

    # Peak hour emergency spike logic
    if 18 <= hour <= 23:
        base_score += 5

    if base_score >= 20:
        return "HIGH"
    elif base_score >= 10:
        return "MODERATE"
    return "LOW"

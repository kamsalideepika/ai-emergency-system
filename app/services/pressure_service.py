def calculate_pressure(accidents: int, ambulance_load: int):
    """
    MVP emergency pressure calculation.
    Later, ML models will replace this.
    """

    # Simple score formula
    score = (accidents * 2) + (ambulance_load * 3)

    if score > 20:
        return "HIGH ALERT 🚨"
    elif score > 10:
        return "MODERATE ⚠️"
    else:
        return "NORMAL ✅"


def generate_alert(level: str):
    """
    Real-time threshold alert system.
    """

    if level == "HIGH":
        return "🚨 ALERT: Emergency overload expected! Deploy extra ambulances."
    elif level == "MODERATE":
        return "⚠️ Warning: Moderate pressure. Monitor resources."
    return "✅ Normal: No overload risk."

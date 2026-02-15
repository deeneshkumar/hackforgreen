def check_thresholds(pm25, co2):
    """
    Checks if values exceed safe thresholds.
    Returns a severity level and a message.
    """
    alerts = []
    
    # PM2.5 Logic
    if pm25 > 250:
        alerts.append({"type": "PM2.5", "severity": "CRITICAL", "message": "Hazardous Air Quality! PM2.5 > 250"})
    elif pm25 > 120:
        alerts.append({"type": "PM2.5", "severity": "HIGH", "message": "Very Poor Air Quality. PM2.5 > 120"})
    elif pm25 > 90:
        alerts.append({"type": "PM2.5", "severity": "MEDIUM", "message": "Poor Air Quality. PM2.5 > 90"})

    # CO2 Logic
    if co2 > 1000:
        alerts.append({"type": "CO2", "severity": "HIGH", "message": "High CO2 Levels! Ventilation Required."})

    return alerts

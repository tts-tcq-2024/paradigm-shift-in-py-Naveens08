TOLERANCE_PERCENTAGE = 0.05

PARAMETER_LIMITS = {
    "temperature": {"min": 0, "max": 45},
    "soc": {"min": 20, "max": 80},
    "charge_rate": {"min": None, "max": 0.8}
}

WARNING_MESSAGES = {
    "temperature": {
        "low": "Warning: Temperature is approaching lower limit!",
        "high": "Warning: Temperature is approaching upper limit!"
    },
    "soc": {
        "low": "Warning: Approaching discharge!",
        "high": "Warning: Approaching charge-peak!"
    },
    "charge_rate": {
        "high": "Warning: Charge rate is approaching upper limit!"
    }
}

WARNING_THRESHOLDS = {
    "temperature": calculate_warning_thresholds("temperature"),
    "soc": calculate_warning_thresholds("soc"),
    "charge_rate": calculate_warning_thresholds("charge_rate")
}

from bms_constants import TOLERANCE_PERCENTAGE, PARAMETER_LIMITS, WARNING_MESSAGES

def calculate_warning_thresholds(param_name):
    limits = PARAMETER_LIMITS[param_name]
    tolerance = (limits["max"] - (limits["min"] if limits["min"] is not None else 0)) * TOLERANCE_PERCENTAGE
    low_warning = limits["min"] + tolerance if limits["min"] is not None else None
    high_warning = limits["max"] - tolerance
    return low_warning, high_warning

WARNING_THRESHOLDS = {
    "temperature": calculate_warning_thresholds("temperature"),
    "soc": calculate_warning_thresholds("soc"),
    "charge_rate": calculate_warning_thresholds("charge_rate")
}

def check_parameter_warning(param_name, value):
    low_warning, high_warning = WARNING_THRESHOLDS[param_name]
    if low_warning is not None and value < low_warning:
        return True, WARNING_MESSAGES[param_name]["low"]
    elif value > high_warning:
        return True, WARNING_MESSAGES[param_name]["high"]
    return True, ''

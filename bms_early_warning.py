from bms_constants import TOLERANCE_PERCENTAGE, PARAMETER_LIMITS, WARNING_MESSAGES, WARNING_THRESHOLDS

def calculate_warning_thresholds(param_name):
    limits = PARAMETER_LIMITS[param_name]
    tolerance = (limits["max"] - (limits["min"] if limits["min"] is not None else 0)) * TOLERANCE_PERCENTAGE
    low_warning = limits["min"] + tolerance if limits["min"] is not None else None
    high_warning = limits["max"] - tolerance
    return low_warning, high_warning
    
def check_low_warning(param_name, value):
    low_warning, _ = WARNING_THRESHOLDS[param_name]
    if low_warning is not None and value < low_warning:
        return True, WARNING_MESSAGES[param_name]["low"]
    return False, ''

def check_high_warning(param_name, value):
    _, high_warning = WARNING_THRESHOLDS[param_name]
    if value > high_warning:
        return True, WARNING_MESSAGES[param_name]["high"]
    return False, ''

def check_parameter_warning(param_name, value):
    low_warning_triggered, low_warning_msg = check_low_warning(param_name, value)
    if low_warning_triggered:
        return True, low_warning_msg
    high_warning_triggered, high_warning_msg = check_high_warning(param_name, value)
    if high_warning_triggered:
        return True, high_warning_msg
    return True, ''

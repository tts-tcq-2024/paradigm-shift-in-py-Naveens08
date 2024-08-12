from bms_constants import PARAMETER_LIMITS

def check_min_limit(param_name, value):
    limits = PARAMETER_LIMITS[param_name]
    min_limit = limits["min"]

    if min_limit is not None and value < min_limit:
        return False, f"{param_name.capitalize()} is below the minimum limit!"
    return True, ''

def check_max_limit(param_name, value):
    limits = PARAMETER_LIMITS[param_name]
    max_limit = limits["max"]

    if value > max_limit:
        return False, f"{param_name.capitalize()} is above the maximum limit!"
    return True, ''

def check_parameter_in_range(param_name, value):
    min_valid, min_msg = check_min_limit(param_name, value)
    if not min_valid:
        return min_valid, min_msg

    max_valid, max_msg = check_max_limit(param_name, value)
    if not max_valid:
        return max_valid, max_msg

    return True, ''

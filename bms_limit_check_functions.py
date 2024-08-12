from bms_early_warning import check_parameter_warning
from bms_constants import PARAMETER_LIMITS
from bms_check_range_functions import check_parameter_in_range

def temperature_check(temperature):
    valid, message = check_parameter_in_range("temperature", temperature)
    if not valid:
        return False, message
    return check_parameter_warning("temperature", temperature)

def state_of_charge_check(soc):
    valid, message = check_parameter_in_range("soc", soc)
    if not valid:
        return False, message
    return check_parameter_warning("soc", soc)

def charge_rate_check(charge_rate):
    valid, message = check_parameter_in_range("charge_rate", charge_rate)
    if not valid:
        return False, message
    return check_parameter_warning("charge_rate", charge_rate)

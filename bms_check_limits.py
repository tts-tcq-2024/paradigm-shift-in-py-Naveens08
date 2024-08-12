# main.py
from battery_checks import temperature_check, state_of_charge_check, charge_rate_check

def battery_is_ok(temperature, soc, charge_rate):
    check_funcs = [temperature_check, state_of_charge_check, charge_rate_check]
    params = [temperature, soc, charge_rate]
    for check_func, param in zip(check_funcs, params):
        valid, message = check_func(param)
        if not valid:
            return False, message
    return True, ''

if __name__ == '__main__':
    try:
        return_val, return_msg = battery_is_ok(25, 70, 0.7)
        assert return_val is True, return_msg
    except AssertionError as e:
        raise AssertionError(f"AssertionError: {e}")

    try:
        return_val, return_msg = battery_is_ok(50, 85, 0)
        assert return_val is True, return_msg
    except AssertionError as e:
        raise AssertionError(f"{e}")

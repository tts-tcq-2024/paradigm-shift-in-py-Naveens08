def temperature_check(temperature):                 
    if temperature < 0 or temperature > 45:
        return False, 'Temperature is out of range!'
    return True, ''
    
def state_of_charge_check(soc):                     
    if soc < 20 or soc > 80:
        return False, 'State of Charge is out of range!'
    return True, ''
    
def charge_rate_check(charge_rate):                 
    if charge_rate > 0.8:
        return False, 'Charge rate is out of range!'
    return True, ''
    
def check_battery_soc(temperature, soc):            
    temp_return_val, temp_return_msg = temperature_check(temperature)
    if not temp_return_val:
        return temp_return_val, temp_return_msg

    soc_return_val, soc_return_msg = state_of_charge_check(soc)
    if not soc_return_val:
        return soc_return_val, soc_return_msg
    
    return True, ''
    
def battery_is_ok(temperature, soc, charge_rate):   
    return_val, return_msg = check_battery_soc(temperature, soc)
    if not return_val:
        return return_val, return_msg
    
    charge_rate_val, charge_rate_msg = charge_rate_check(charge_rate)
    if not charge_rate_val:
        return charge_rate_val, charge_rate_msg
    
    return True, ''

if __name__ == '__main__':
    return_val, return_msg = battery_is_ok(25, 70, 0.7)
    assert return_val is True, return_msg
    
    return_val, return_msg = battery_is_ok(50, 85, 0)
    assert return_val is True, return_msg

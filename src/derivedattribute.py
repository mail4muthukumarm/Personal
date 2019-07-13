from enum import Enum
'''
This is a python module which has computing functions using the below parameters
1. Temperature
2. Pressure
3. RH  
'''


class Condition(Enum):
    RAIN = 1
    SNOW = 2
    SUNNY = 3


'''
This function calculates the atmospheric conditions.
'''
def compute_AtmosphericCondition(temp,rh):
    if temp < 0 or rh > 0:
        return Condition.SNOW
    elif (temp > 0 and temp <20) and (rh > 40 and rh < 60):
        return Condition.RAIN
    else:
        return Condition.SUNNY

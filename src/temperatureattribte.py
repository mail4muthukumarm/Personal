from environmentattribute import  EnvironmentAttribute
import numbers

'''
    This class calculates temperature from elevation and SST
'''


class TemperatureAttribute(EnvironmentAttribute):

    def __init__(self,lat, alt):
        super(TemperatureAttribute, self).__init__(alt)
        self._latitude = lat
        self._temperature_lapse_constant = 3.5
        self._lat_sst_ref = {"-60": 4, "-45": 15, "-30": 24, "-15": 30, "0": 32, "15": 25, "30": 20, "45": 6, "75": 4}

    '''
    Public method to calculate temperature.
    '''
    def calculate(self):
        if not isinstance(self._latitude, numbers.Number):
            return "Invalid Inputs"

        if not isinstance(self.altitude, numbers.Number) or self.altitude <= 0:
            return "Invalid Inputs"

        try:
            ref_temp = self._calculate_sst()
            return ref_temp - (self._temperature_lapse_constant * self.altitude)
        except Exception as e:
            raise e

    '''
    Private method to calculate sea surface temperature(SST). This is one of the input
    for temperature calculation.
    '''
    def _calculate_sst(self):
        delta = 1000 # Initializing to random high value
        try:
            for k,v in self._lat_sst_ref.items():
                temp = abs(float(self._latitude) - float(k))
                if temp < delta:
                    delta = temp
                    sst = v
            return sst
        except Exception as e:
            raise e






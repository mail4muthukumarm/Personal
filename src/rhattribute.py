from environmentattribute import EnvironmentAttribute
import numbers

'''
This class calculates relative humidity using air temperature and dew point (based on assumption)
'''


class RHAttribute(EnvironmentAttribute):

    def __init__(self, alt):
        super(RHAttribute, self).__init__(alt)

    @property
    def temperature(self):
        return self._temp_tb

    @temperature.setter
    def temperature(self, value):
        self._temp_tb = value

    def calculate(self):
        if not isinstance(self.temperature, numbers.Number):
            return "Invalid Inputs"
        actual_vp = 6.11 * (10*((7.5*self.temperature)/(237.3+self.temperature)))
        std_vp = 6.11 * (10 * ((7.5 * (self.temperature-3)) / (237.3 + (self.temperature-3))))
        return round(actual_vp/std_vp)*100
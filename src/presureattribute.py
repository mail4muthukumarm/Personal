from environmentattribute import EnvironmentAttribute
import numbers

'''
This class calculates pressure using barometric principle
'''


class PressureAttribute(EnvironmentAttribute):

    def __init__(self, alt):
        self._temperature_lapse_constant_lb = 0.0065
        self._gas_constant_r = 8.31447
        self._molar_mass_m = 0.0289644
        self._gravity_g0 = 9.80665
        self.height_bottom_hb = 0
        self.static_press_pb= 101325.0
        super(PressureAttribute,self).__init__(alt)

    @property
    def temperature(self):
        return self._temp_tb

    @temperature.setter
    def temperature(self,value):
        self._temp_tb = value

    def calculate(self):
        if not isinstance(self.altitude, numbers.Number) or self.altitude <= 0:
            return "Invalid Inputs"

        if not isinstance(self.temperature, numbers.Number):
            return "Invalid Inputs"

        # Applying barometric formula
        pressure = self.static_press_pb * \
                   pow((self._temp_tb/(self._temp_tb+(self._temperature_lapse_constant_lb *
                                      (self.altitude-self.height_bottom_hb)))),
                       ((self._gravity_g0 * self._molar_mass_m)/(self._gas_constant_r *
                        self._temperature_lapse_constant_lb)))
        return abs(pressure)/100



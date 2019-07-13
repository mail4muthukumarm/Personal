from derivedattribute import *

'''
    This class represents a particular point.
'''


class Point(object):

    # Parameterised constructor with Dependency injection pattern
    def __init__(self, temp_processor=None, press_processor=None, rh_processor=None):
        self._temp_processor = temp_processor
        self._press_processor = press_processor
        self._rh_processor = rh_processor

    def __str__(self):
        if self.status == '':
            self._temperature = self._temp_processor.calculate()
            self._press_processor.temperature = self._temperature
            self._pressure = self._press_processor.calculate()
            self._rh_processor.temperature = self._temperature
            self._rh = self._rh_processor.calculate()
            self._condition = compute_AtmosphericCondition(self.temperature,self.relative_humidity)
            try:
                return self.point_name + "|" + str(self.latitude) +","+ str(self.longitude) +","+ str(self.altitude)\
                   +"|"+ str(self.time)+"|"+str(self.condition)+"|"+str(self.temperature)+"deg.cel"+\
                   "|"+str(self.pressure)+'hPa'+"|"+str(self.relative_humidity)+"%"
            except Exception as e:
                print(e.message)
        else:
            return self.point_name + "|" + self.latitude+","+self.longitude+","+ self.status

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self,value):
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def point_name(self):
        return self._pointname

    @point_name.setter
    def point_name(self, value):
        self._pointname = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        self._pressure = value

    @property
    def relative_humidity(self):
        return self._rh

    @relative_humidity.setter
    def relative_humidity(self, value):
        self._rh = value

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self,value):
        self._altitude = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self,value):
        self._time = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value










'''
Base class for all environment attribute(s)
'''


class EnvironmentAttribute(object):

    def __init__(self,alt):
        self._altitude = alt

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self,value):
        self._altitude = value

    def calculate(self):
        pass


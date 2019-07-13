from point import Point
from environmentattribute import EnvironmentAttribute
from temperatureattribte import TemperatureAttribute
from presureattribute import PressureAttribute
from rhattribute import RHAttribute
from adaptor import *

'''
This class represents the collection of point object
'''


class Points(list):

    def __init__(self, file_path):
        self._path = file_path

    def read(self):
        file_handle = open(self._path, 'r')
        for line in file_handle:
            fields = line.split(',')
            name = fields[0]
            try:
                lat = float(fields[1])
                long = float(fields[2].strip('\n'))
                alt, status, error = compute_altitude(lat, long)
            except Exception as e:
                status = 400 # Invalid input
                error = "Invalid Inputs"

            if(status != 200):
                point = Point()
                point.status = error
            else:
                temp_attr = TemperatureAttribute(lat,alt)
                press_attr = PressureAttribute(alt)
                rh_attr = RHAttribute(alt)
                point = Point(temp_attr,press_attr,rh_attr)
                point.point_name = name
                point.latitude = lat
                point.longitude = long
                point.altitude = alt
                point.status = ''
                point.time = compute_timezone(lat,long)
            super(Points, self).append(point)
        file_handle.close()




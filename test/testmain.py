from temperatureattribute_testcase import *
from pressureattribute_testcase import *
from rhattribute_testcase import  *
from points_testcase import *

import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TemperatureAttributeTestCase('test_calculate'))
    suite.addTest(PressureAttributeTestCase('test_calculate'))
    suite.addTest(RHAttributeTestCase('test_calculate'))
    suite.addTest(PointsTestCase('test_read'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
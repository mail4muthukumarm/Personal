import temperatureattribte
from temperatureattribte import TemperatureAttribute
import unittest

class TemperatureAttributeTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_attr_1 = TemperatureAttribute("wew",22)
        self.temp_attr_2 = TemperatureAttribute(23, 22)

    def test_calculate(self):
        self.assertIsInstance( self.temp_attr_1 , TemperatureAttribute)
        self.assertEquals(self.temp_attr_1.calculate(),"Invalid Inputs")
        self.assertIsInstance(self.temp_attr_2, TemperatureAttribute)
        self.assertEquals(self.temp_attr_2.calculate(),-57.0)

    def tearDown(self):
        del self.temp_attr_1
        del self.temp_attr_2
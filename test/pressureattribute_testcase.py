
from presureattribute import PressureAttribute
import unittest

class PressureAttributeTestCase(unittest.TestCase):
    def setUp(self):
        self.press_attr_1 = PressureAttribute("wew")
        self.press_attr_2 = PressureAttribute(50)
        self.press_attr_3 = PressureAttribute(-4)
        self.press_attr_1.temperature = 20
        self.press_attr_2.temperature = 20
        self.press_attr_3.temperature = 20


    def test_calculate(self):
        self.assertIsInstance( self.press_attr_1 , PressureAttribute)
        self.assertEquals(self.press_attr_1.calculate(),"Invalid Inputs")
        self.assertIsInstance(self.press_attr_2, PressureAttribute)
        self.assertEquals(self.press_attr_2.calculate(),930.9432502919495)
        self.assertIsInstance(self.press_attr_3, PressureAttribute)
        self.assertEquals(self.press_attr_1.calculate(),"Invalid Inputs")

    def tearDown(self):
        del self.press_attr_1
        del self.press_attr_2
        del self.press_attr_3
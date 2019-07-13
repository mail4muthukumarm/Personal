import rhattribute
from rhattribute import RHAttribute
import unittest

class RHAttributeTestCase(unittest.TestCase):
    def setUp(self):
        self.rh_attr_1 = RHAttribute(22)
        self.rh_attr_2 = RHAttribute(22)
        self.rh_attr_1.temperature = 'hi'
        self.rh_attr_2.temperature = 23

    def test_calculate(self):
        self.assertIsInstance( self.rh_attr_1 , RHAttribute)
        self.assertEquals(self.rh_attr_1.calculate(),"Invalid Inputs")
        self.assertIsInstance(self.rh_attr_2, RHAttribute)
        self.assertEquals(self.rh_attr_2.calculate(),100)

    def tearDown(self):
        del self.rh_attr_1
        del self.rh_attr_2
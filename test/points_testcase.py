
from points import Points
import unittest

class PointsTestCase(unittest.TestCase):
    def setUp(self):
        self.points = Points("testinput.txt")

    def test_read(self):
        self.assertEquals(self.points.read(),None)
        for point in self.points:
            self.assertEquals(point.status,"Invalid Inputs")

    def tearDown(self):
        del self.points

import unittest
from src.circle import area, perimeter
import math

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2.1), math.pi * 2.1**2)

    def test_area_negative_radius(self):
        self.assertRaises(ValueError, area, -1)
    
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(2.1), 2 * math.pi * 2.1)

    def test_perimeter_negative_radius(self):
        self.assertRaises(ValueError, perimeter, -1)

    def test_wrong_types_area(self):
        self.assertRaises(TypeError, area, '1')
        self.assertRaises(TypeError, area, [1])
        self.assertRaises(TypeError, area, True)

    def test_wrong_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, '1')
        self.assertRaises(TypeError, perimeter, [1])
        self.assertRaises(TypeError, perimeter, True)

if __name__ == '__main__':
    unittest.main()

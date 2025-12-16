import math
import unittest

def area(r):
    # Возвращает площадь круга. Принимает значение r - радиус круга
    return math.pi * r * r


def perimeter(r):
    # Возвращает длинну окружности. Принимает значение r - радиус круга.
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
  def test_zero_mul(self):
    res = area(0)
    self.assertEqual(res, 0)
  
  def test_square_mul(self):
    res = area(10)
    self.assertEqual(res, math.pi * 100)

  def test_negative_mul(self):
    res = area(-5)
    self.assertEqual(res, math.pi * 25)

  def test_rational_mul(self):
    res = area(1.5)
    self.assertEqual(res, math.pi * 2.25)

  def test_large_number_mul(self):
    res = area(43391040458)
    self.assertEqual(res, math.pi * 1882782392027792849764)

  def test_simple_perimeter(self):
    res = perimeter(78)
    self.assertEqual(res, math.pi * 156)

  def test_negative_radius_perimetr(self):
    res = perimeter(-5)
    self.assertEqual(res, math.pi * 10)

  def test_null_radius_perimeter(self):
    res = perimeter(0)
    self.assertEqual(res, 0)

  def test_rational_radius_perimeter(self):
    res = perimeter(3.7)
    self.assertEqual(res, math.pi * 7.4)

  def test_large_perimeter(self):
    res = perimeter(43391040458)
    self.assertEqual(res, math.pi * 86782080916)
import unittest

def area(a):
    # Возвращает площадь квадрата. Принимает a - длинна стороны квадрата
    return a * a


def perimeter(a):
    # Возвращает периметр квадрата. Принимает a - длинна стороны квадрата
    return 4 * a

class RectangleTestCase(unittest.TestCase):
  def test_zero_mul(self):
    res = area(0)
    self.assertEqual(res, 0)
  
  def test_square_mul(self):
    res = area(10)
    self.assertEqual(res, 100)

  def test_negative_mul(self):
    res = area(-5)
    self.assertEqual(res, 25)

  def test_rational_mul(self):
    res = area(1.5)
    self.assertEqual(res, 2.25)

  def test_large_number_mul(self):
    res = area(43391040458)
    self.assertEqual(res, 1882782392027792849764)

  def test_simple_perimeter(self):
    res = perimeter(78)
    self.assertEqual(res, 312)

  def test_negative_side_perimetr(self):
    res = perimeter(-5)
    self.assertEqual(res, 20)

  def test_null_side_perimeter(self):
    res = perimeter(0)
    self.assertEqual(res, 0)

  def test_rational_sides_perimeter(self):
    res = perimeter(8.9)
    self.assertEqual(res, 35.6)

  def test_large_perimeter(self):
    res = perimeter(43391040458)
    self.assertEqual(res, 173564161832)
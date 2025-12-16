import unittest

def area(a, h):
    # Возвращает площадь треугольника.
    # Принимает a - длинну стороны основания и h - длинну высоты 
    return a * h / 2 

def perimeter(a, b, c):
    # Возвращает периметр треугольника.
    # Принимает a, b, c - длины сторон треугольника
    return a + b + c 


class TriangleTestCase(unittest.TestCase):
  def test_zero_mul(self):
    res = area(10, 0)
    self.assertEqual(res, 0)
  
  def test_square_mul(self):
    res = area(10, 10)
    self.assertEqual(res, 50)

  def test_negative_mul(self):
    res = area(10, -5)
    self.assertEqual(res, 25)

  def test_2_negative_mul(self):
    res = area(-4, -9)
    self.assertEqual(res, 18)

  def test_rational_mul(self):
    res = area(1.5, 0.01)
    self.assertEqual(res, 0.0075)

  def test_large_number_mul(self):
    res = area(2343464623, 43391040458)
    self.assertEqual(res, 50842684134242358667)

  def test_equal_sides_perimeter(self):
    res = perimeter(78, 78, 100)
    self.assertEqual(res, 256)

  def test_negative_side_perimeter(self):
    res = perimeter(-5, 10, 7)
    self.assertEqual(res, 22)

  def test_2_negative_sides_perimeter(self):
    res = perimeter(-7, -10, 45)
    self.assertEqual(res, 62)

  def test_3_negative_sides_perimeter(self):
    res = perimeter(-10, -10, -10)
    self.assertEqual(res, 30) 

  def test_null_side_perimeter(self):
    res = perimeter(45, 0, 5)
    self.assertEqual(res, 50)

  def test_rational_sides_perimeter(self):
    res = perimeter(3.7, 8.9, 10)
    self.assertEqual(res, 22.6)

  def test_large_perimeter(self):
    res = perimeter(2343464623, 43391040458, 10004000030)
    self.assertEqual(res, 55738505111)
import unittest

def area(a, b):
    # Возвращает площадь прямоугольника. 
    # Принимает значения a, b - стороны прямоугольника
    return a * b 

def perimeter(a, b): 
    # Возвращает периметр прямоугольника. 
    # Принимает значения a, b - стороны прямоугольника
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
  def test_zero_mul(self):
    res = area(10, 0)
    self.assertEqual(res, 0)
  
  def test_square_mul(self):
    res = area(10, 10)
    self.assertEqual(res, 100)

  def test_negative_mul(self):
    res = area(10, -5)
    self.assertEqual(res, 50)

  def test_2_negative_mul(self):
    res = area(-4, -9)
    self.assertEqual(res, 36)

  def test_rational_mul(self):
    res = area(1.5, 0.01)
    self.assertEqual(res, 0.015)

  def test_large_number_mul(self):
    res = area(2343464623, 43391040458)
    self.assertEqual(res, 101685368268484717334)

  def test_equal_sides_perimeter(self):
    res = perimeter(78, 78)
    self.assertEqual(res, 312)

  def test_negative_side_perimetr(self):
    res = perimeter(-5, 10)
    self.assertEqual(res, 30)

  def test_2_negative_sides(self):
    res = perimeter(-7, -10)
    self.assertEqual(res, 34)

  def test_null_side_perimeter(self):
    res = perimeter(45, 0)
    self.assertEqual(res, 45)

  def test_rational_sides_perimeter(self):
    res = perimeter(3.7, 8.9)
    self.assertEqual(res, 25.2)

  def test_large_perimeter(self):
    res = perimeter(2343464623, 43391040458)
    self.assertEqual(res, 91469010162)
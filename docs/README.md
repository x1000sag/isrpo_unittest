# Общее описание решения
Эта библиотека содержит функции для расчёта площадей и периметров различных геометрических фигур. \ 
Скрипты в репозитории: \
+ [circle](../circle.py)
+ [rectangle](../rectangle.py)
+ [square](../square.py)
+ [triangle](../triangle.py)
# Функции
1. [circle](../circle.py)
  + area(r) Возвращает площадь круга. Принимает значение r - радиус круга.
  + perimeter(r) Возвращает длинну окружности. Принимает значение r - радиус круга.
2. [rectangle](../rectangle.py)
  + area(a, b) Возвращает площадь прямоугольника. \ Принимает значения a, b - стороны прямоугольника.
  + perimeter(a, b): Возвращает периметр прямоугольника. \ Принимает значения a, b - стороны прямоугольника.
3. [square](../square.py)
  + area(a) Возвращает площадь квадрата. Принимает a - длинна стороны квадрат.
  + perimeter(a) Возвращает периметр квадрата. Принимает a - длинна стороны квадрата.
4. [triangle](../triangle.py)
  + area(a, h) Возвращает площадь треугольника. \ Принимает a - длинну стороны основания и h - длину высоту.
  + perimeter(a, b, c) Возвращает периметр треугольника. \ Принимает a, b, c - длинны сторон треугольника.
# Unit тесты
1. [circle](../circle.py)
  + `test_zero_mul` - тест на нулевой радиус
  + `test_square_mul` - тест на площадь при радиусе 10
  + `test_negative_mul` - тест на отрицательный радиус
  + `test_rational_mul` - тест на дробный радиус
  + `test_large_number_mul` - тест на большой радиус
  + `test_simple_perimeter` - тест на периметр при радиусе 78
  + `test_negative_radius_perimetr` - тест на периметр при отрицательном радиусе
  + `test_null_radius_perimeter` - тест на периметр при нулевом радиусе
  + `test_rational_radius_perimeter` - тест на периметр при дробном радиусе
  + `test_large_perimeter` - тест на периметр при большом радиусе

2. [square](../square.py)
  + `test_zero_mul` - тест на нулевую сторону
  + `test_square_mul` - тест на площадь при стороне 10
  + `test_negative_mul` - тест на отрицательную сторону
  + `test_rational_mul` - тест на дробную сторону
  + `test_large_number_mul` - тест на большую сторону
  + `test_simple_perimeter` - тест на периметр при стороне 78
  + `test_negative_side_perimetr` - тест на периметр при отрицательной стороне
  + `test_null_side_perimeter` - тест на периметр при нулевой стороне
  + `test_rational_sides_perimeter` - тест на периметр при дробной стороне
  + `test_large_perimeter` - тест на периметр при большой стороне

3. [triangle](../triangle.py)
  + `test_zero_mul` - тест на нулевую высоту при основании 10
  + `test_square_mul` - тест на площадь при основании и высоте 10
  + `test_negative_mul` - тест на отрицательную высоту
  + `test_2_negative_mul` - тест на отрицательные основание и высоту
  + `test_rational_mul` - тест на дробные основание и высоту
  + `test_large_number_mul` - тест на большие основание и высоту
  + `test_equal_sides_perimeter` - тест на периметр с двумя равными сторонами
  + `test_negative_side_perimeter` - тест на периметр с одной отрицательной стороной
  + `test_2_negative_sides_perimeter` - тест на периметр с двумя отрицательными сторонами
  + `test_3_negative_sides_perimeter` - тест на периметр с тремя отрицательными сторонами
  + `test_null_side_perimeter` - тест на периметр с нулевой стороной
  + `test_rational_sides_perimeter` - тест на периметр с дробными сторонами
  + `test_large_perimeter` - тест на периметр с большими сторонами

4. [rectangle](../rectangle.py)
  + `test_zero_mul` - тест на нулевую сторону
  + `test_square_mul` - тест на площадь при сторонах 10 и 10
  + `test_negative_mul` - тест на отрицательную сторону
  + `test_2_negative_mul` - тест на две отрицательные стороны
  + `test_rational_mul` - тест на дробные стороны
  + `test_large_number_mul` - тест на большие стороны
  + `test_equal_sides_perimeter` - тест на периметр с равными сторонами
  + `test_negative_side_perimetr` - тест на периметр с одной отрицательной стороной
  + `test_2_negative_sides` - тест на периметр с двумя отрицательными сторонами
  + `test_null_side_perimeter` - тест на периметр с нулевой стороной
  + `test_rational_sides_perimeter` - тест на периметр с дробными сторонами
  + `test_large_perimeter` - тест на периметр с большими сторонами
# История изменения проекта
## Ветка main
+ `8ba9aeb` - L-03: Circle and square added
+ `d078c8d` - L-03: Docs added
## Ветка develop
+ `d080c78` - L-04: Triangle added
+ `51c40eb` - L-04: Doc updated for triangle
+ `d76db2a` - L-04: Add calculate.py
+ `b5b0fae` - L-04: Update docs for calculate.py
## Ветка feature
+ `3049431` - L-04: Add rectangle.py
## Ветка release
+ `6adb962` - L-03: Docs added
+ `438b89a` - L-05: Add user agreement
+ `86edb1c` - L-05: Update Docs. Add user agreement info
## Ветка new_features_504628
+ `7c04dd4` - Added rectangle.py
+ `b51b135` - Added triangle.py and fixed perimeter() in rectangle.py
## Ветка unittest
+ `781aa90` - added rectangle unit test
+ `3e2f648` - added circle unit test
+ `a8f148f` - added unit test for triangle.py
+ `01c7637` - Added square unit test
## CICD
Добавлен CICD.yml
 
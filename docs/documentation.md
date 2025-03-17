# Библиотека для работы с геометрическими фигурами

## Модуль [circle.py](../src/circle.py)
### Функция area(r: float) -> float
Вычисляет площадь круга с радиусом r. 
Пример использования:
```python
from circle import area
area(5) # 78.53...
```

### Функция perimeter(r: float) -> float
Вычисляет периметр круга с радиусом r.
Пример использования:
```python
from circle import perimeter
perimeter(5) # 31.41...
```

## Модуль [rectangle.py](../src/rectangle.py)
### Функция area(a: float, b: float) -> float
Вычисляет площадь прямоугольника со сторонами a и b.
Пример использования:
```python
from rectangle import area
area(5, 10) # 50
```

### Функция perimeter(a: float, b: float) -> float
Вычисляет периметр прямоугольника со сторонами a и b.
Пример использования:
```python
from rectangle import perimeter
perimeter(5, 10) # 30
```

## Модуль [square.py](../src/square.py)
### Функция area(a: float) -> float
Вычисляет площадь квадрата со стороной a.
Пример использования:
```python
from square import area
area(5) # 25
```

### Функция perimeter(a: float) -> float
Вычисляет периметр квадрата со стороной a.
Пример использования:
```python
from square import perimeter
perimeter(5) # 20
```
## Модуль [triangle.py](../src/triangle.py)
### Функция area(a: float, b: float, c: float) -> float
Вычисляет площадь треугольника со сторонами a, b и c.
Пример использования:
```python
from triangle import area
area(3, 4, 5) # 6.0
```

### Функция perimeter(a: float, b: float, c: float) -> float
Вычисляет периметр треугольника со сторонами a, b и c.
Пример использования:
```python
from triangle import perimeter
perimeter(3, 4, 5) # 12
```

### Список коммитов:
```shell
0a3f517 (HEAD -> documentations, origin/new_features_409124) I dont know why triangle.py dont added in commit before
3912f84 fix perimeter in rectangle.py and add triange.py
1d91c62 Add new file rectangle.py
d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
8ba9aeb L-03: Circle and square added
```

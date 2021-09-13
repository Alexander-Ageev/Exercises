import random

class figure:
    def __init__(self, points):
        self._points = points
        self._lenghts = []         
    def square(self):
        # вычисляем площадь квадрата
        print(f'Площадь квадрата: a * b')
    def perimeter(self):
        return sum(self._lenghts)

class triangle(figure):
    def __init__(self, points):
        super().__init__(points)
        self.__hight = 0
        self.__hight_calc()
        print(f'#Объект создан') # проверка успешного создания объекта подкласса треугольник
    def __hight_calc(self):
        # вычисление высоты треугольника
        print('#__hight_calc started') # проверка успешного вызова метода
        self.__hight = 1 
        print(f'#Высота треугольника: {self.__hight}')
        print('#__hight_calc done') # проверка успешного выполнения метода
    def square(self):
        # вычисление площади треугольника
        assert self.__hight != 0 # проверка нужна для исключения работы с некорректными размерами фигуры
        print(f'Плошадь треугольника: (a * h)/2')

class circle(figure):
    def __init__(self, points):
        super().__init__(points)
        self.__radius = 0  
        self.__radius_calc()  
    def __radius_calc(self):
        # вычисление радиуса
        self.__radius = 2
        print(f'Радиус круга {self.__radius}')
    def square(self):
        assert self.__radius != 2 #условие для проверки работы assert
        print(f'Площадь круга: pi * r * r')
    def perimeter (self):
        return 2 * 3.14 * self.__radius

TRIANGLE = 0
CIRCLE = 1
figures = []

for i in range(10):
    rnd = random.randint(0, 1)
    if rnd == TRIANGLE:
        figures.append(triangle([ (j+1) * (i+1) for j in range(6)]))
        print('#Треугольник создан')
        print(f'#{figures[i]._points}\n')
    elif rnd == CIRCLE:
        figures.append(circle([ (j+1) * (i+1) for j in range(4)]))
        print('#Круг создан')
        print(f'#{figures[i]._points}\n')

print('\nВывод результатов работы программы:')
for i in range(len(figures)):
    figures[i].square()
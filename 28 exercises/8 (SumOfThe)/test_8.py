import unittest
from main import SumOfThe
import random

class main_tests(unittest.TestCase):
    def test_regression_simple(self):
        data = [100, -50, 10, -25, 90, -35, 90]
        res = 90
        self.assertEqual(SumOfThe(len(data), data), res)
    def test_regression_mixed(self):
        data = [10, -25, -45, -35, 5]
        res = -45
        self.assertEqual(SumOfThe(len(data), data), res)
# Случайное тестирование, охватывает логичные комбинации кроме комбинаций с пустыми строками
    def test_random(self):
        for i in range(50000):
            element_number = random.randint(1, 9)
            data = []
            for j in range(element_number):
                mode = random.choice([-1, 1])        
                number = random.randint(1, 100)
                data.append(int(mode*number))
            data.append(sum(data))
            res = data[-1]
            self.assertEqual(SumOfThe(len(data), data), res)
# Тестирование значениями одного элемента
    def test_one_input_element(self):
        data = [10, 10]
        res = 10
        self.assertEqual(SumOfThe(len(data), data), res)


if __name__ == '__main__':
    unittest.main()
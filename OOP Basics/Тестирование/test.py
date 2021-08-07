import unittest
from main import function
from random import randint

class main_tests(unittest.TestCase):
    def test_regression_true(self):# точно истинный вариант
        s1 = '1234567'
        s2 = '456'        
        self.assertEqual(function(s1, s2), s1.find(s2))
    def test_regression_false(self):# точно ложный вариант
        s1 = '1234567'
        s2 = '46'
        self.assertEqual(function(s1, s2), s1.find(s2))
# Случайное тестирование, охватывает логичные комбинации кроме комбинаций с пустыми строками
    def test_random(self):
        for i in range(500):
            s1 = str(randint(0,1000000))
            s2 = str(randint(0,1000000))
            self.assertEqual(function(s1, s2), s1.find(s2))
# Тестирование нулевыми значениями
    def test_null_s1(self):
        s1 = ''
        s2 = "123"
        self.assertEqual(function(s1, s2), s1.find(s2))
    def test_null_s2(self):
        s1 = '123'
        s2 = ''
        self.assertEqual(function(s1, s2), s1.find(s2))
    def test_nul_all(self):# компромиссный вариант
        s1 = ''
        s2 = ''
        self.assertEqual(function(s1, s2), s1.find(s2))
# Тестирование максимальными значениями
    def test_max(self):
        s1 = ''
        for i in range(100000):
            s1 += str(randint(0,9))
        s2 = '1234567'
        self.assertEqual(function(s1, s2), s1.find(s2))
# Тестирование, когда len(s1) < len(s2)
    def test_s2_bigger(self):
        s1 = '123'
        s2 = '12345'
        self.assertEqual(function(s1, s2), s1.find(s2))
# Тестирование для случая s1 = s2
    def test_equal(self):
        s1 = '12345'
        self.assertEqual(function(s1, s1), s1.find(s1))

if __name__ == '__main__':
    unittest.main()
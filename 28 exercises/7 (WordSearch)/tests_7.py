import unittest
from main import WordSearch
import random

class main_tests(unittest.TestCase):
    def test_regression_true(self):
        length = 12
        s = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
        subs = 'строк'
        outp = [0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(WordSearch(length, s, subs), outp)
    
    def test_regression_translit(self):
        length = 12
        s = '1) stroka razbivaetsya na nabor strok cherez vyravnivanie po zadannoj shirine.'
        subs = 'strok'
        outp = [0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(WordSearch(length, s, subs), outp)
    
    def test_regression_start(self):
        length = 3
        s = '12345'
        subs = '123'
        outp = [1, 0]
        self.assertEqual(WordSearch(length, s, subs), outp)
    
    def test_regression_end(self):
        length = 3
        s = '12345'
        subs = '45'
        outp = [0, 1]
        self.assertEqual(WordSearch(length, s, subs), outp)

    def test_regression_false(self):# точно ложный вариант
        length = 12
        s = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
        subs = 'Строк'
        outp = [0, 0, 0, 0, 0, 0, 0]
        self.assertEquals(WordSearch(length, s, subs), outp)
    def test_regression_min_list(self):
        length = 75
        s = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
        subs = 'строк'
        outp = [1]
        self.assertEqual(WordSearch(length, s, subs), outp)

# Случайное тестирование, охватывает логичные комбинации кроме комбинаций с пустыми строками


# Тестирование нулевыми значениями входящей строки
    def test_null(self):
        length = 12
        s = ''
        subs = 'строк'
        outp = []
        self.assertEqual(WordSearch(length, s, subs), outp)

# Тестирование максимальными значениями
    


if __name__ == '__main__':
    unittest.main()
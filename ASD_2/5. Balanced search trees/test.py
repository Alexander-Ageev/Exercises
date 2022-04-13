"""Тесты для функции балансировки бинарного дерева поиска"""
import unittest
import random
from main import GenerateBBSTArray

class MainTest(unittest.TestCase):
    def test_tree(self):
        """Проверка несортированным тестовым деревом"""
        array = [i+1 for i in range(15)]
        random.shuffle(array)
        res = GenerateBBSTArray(array)
        data = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(res, data)

    def test_one_element_tree(self):
        """Проверка деревом, состощим из корня"""
        array = [1]
        res = GenerateBBSTArray(array)
        data = [1]
        self.assertEqual(res, data)

    def test_zero_tree(self):
        """Проверка пустым деревом"""
        array = []
        res = GenerateBBSTArray(array)
        data = []
        self.assertEqual(res, data)

    def test_not_full_tree(self):
        """Проверка неполным деревом"""
        array = [1, 2, 4, 5, 6]
        res = GenerateBBSTArray(array)
        data = [4, 2, 6, 1, 5]
        self.assertEqual(res, data)

if __name__ == '__main__':
    unittest.main()

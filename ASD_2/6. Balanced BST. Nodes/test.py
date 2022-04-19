"""Тесты для функции балансировки бинарного дерева поиска, реализованного через узлы"""
import unittest
import random
from main import BalancedBST

class MainTest(unittest.TestCase):
    def test_tree(self):
        """Проверка несортированным тестовым деревом"""
        tree = BalancedBST()
        array = [i+1 for i in range(15)]
        random.shuffle(array)
        tree.GenerateTree(array)
        res = tree.ListNodes()
        data = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(res, data)


if __name__ == '__main__':
    unittest.main()

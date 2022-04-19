"""Тесты для функции балансировки бинарного дерева поиска, реализованного через узлы"""
import unittest
import random
from main import BalancedBST

NODES = [8, 3, 10, 1, 6, 14, 4, 7, 13]

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

    def test_is_balance_true(self):
        """Проверка сбалансированной ветки"""
        tree = BalancedBST()
        for node in NODES:
            tree.AddKeyValue(node)
        node = tree.FindNodeByKey(3).Node
        res = tree.IsBalanced(node)
        data = True
        self.assertEqual(res, data)

    def test_is_balance_true_2(self):
        """Проверка сбалансированной ветви без потомков"""
        tree = BalancedBST()
        for node in NODES:
            tree.AddKeyValue(node)
        node = tree.FindNodeByKey(1).Node
        res = tree.IsBalanced(node)
        data = True
        self.assertEqual(res, data)

    def test_is_balance_false_1(self):
        """Проверка несбалансированного дерева,
        максимальная глубина поддеревьев одинаковая,
        но ветвь 10 -> 14 -> 13 несбалансирована"""
        tree = BalancedBST()
        for node in NODES:
            tree.AddKeyValue(node)
        node = tree.FindNodeByKey(8).Node
        res = tree.IsBalanced(node)
        data = False
        self.assertEqual(res, data)

    def test_is_balance_false_2(self):
        """Проверка несбалансированной ветви"""
        tree = BalancedBST()
        for node in NODES:
            tree.AddKeyValue(node)
        node = tree.FindNodeByKey(10).Node
        res = tree.IsBalanced(node)
        data = False
        self.assertEqual(res, data)

if __name__ == '__main__':
    unittest.main()

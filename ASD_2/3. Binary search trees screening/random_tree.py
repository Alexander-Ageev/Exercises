"""Тесты для методов обхода бинарного дерева поиска"""
import unittest
import random
from main import BSTNode, BST

ELEMENTS_COUNT = random.randint(0, 9) + 1
ROOT = 0

class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        """Автоматическая генерация тестового дерева. Проверка метода AddKeyValue"""
        root = BSTNode(ROOT, ROOT, None)
        tree = BST(root)
        keys = [0]
        for i in range(ELEMENTS_COUNT):
            random_key = random.randint(-10, 10)
            keys.append(random_key)
            tree.AddKeyValue(random_key, random_key)
        self.keys = keys
        self.root = root
        self.tree = tree

    def test_wide(self):
        """Проверка обхода дерева в ширину"""
        nodes = self.tree.WideAllNodes()
        res = self.tree.ListNodes(nodes)
        print('keys: ', self.keys)
        print('wide-order: ', res, '\n')
        data = []
        self.assertEqual(res, data)

    def test_deep_in_order(self):
        """Проверка обхода дерева в глубину. In-order"""
        nodes = self.tree.DeepAllNodes(0)
        res = self.tree.ListNodes(nodes)
        print('keys: ', self.keys)
        print('in-order: ', res, '\n')
        data = []
        self.assertEqual(res, data)

    def test_deep_post_order(self):
        """Проверка обхода дерева в глубину. Post-order"""
        nodes = self.tree.DeepAllNodes(1)
        res = self.tree.ListNodes(nodes)
        print('keys: ', self.keys)
        print('post-order: ', res, '\n')
        data = []
        self.assertEqual(res, data)

    def test_deep_pre_order(self):
        """Проверка обхода дерева в глубину. Pre-order"""
        nodes = self.tree.DeepAllNodes(2)
        res = self.tree.ListNodes(nodes)
        print('keys: ', self.keys)
        print('pre-order: ', res, '\n')
        data = []
        self.assertEqual(res, data)

if __name__ == "__main__":
    unittest.main()

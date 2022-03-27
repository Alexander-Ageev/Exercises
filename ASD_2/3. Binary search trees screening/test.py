"""Тесты для методов обхода бинарного дерева поиска"""
import unittest
from main import BSTNode, BST

NODES = [4, 12, 2, 6, 14, 1, 3, 7, 13]
ELEMENTS_COUNT = len(NODES) + 1
ROOT = 8

class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        """Автоматическая генерация тестового дерева. Проверка метода AddKeyValue"""
        root = BSTNode(ROOT, ROOT, None)
        tree = BST(root)
        for i in NODES:
            tree.AddKeyValue(i, i)
        self.root = root
        self.tree = tree

    def test_wide(self):
        """Проверка обхода дерева в ширину"""
        nodes = self.tree.WideAllNodes()
        res = self.tree.ListNodes(nodes)
        data = [8, 4, 12, 2, 6, 14, 1, 3, 7, 13]
        self.assertEqual(res, data)

    def test_deep_in_order(self):
        """Проверка обхода дерева в глубину. In-order"""
        nodes = self.tree.DeepAllNodes(0)
        res = self.tree.ListNodes(nodes)
        data = [8, 4, 2, 1, 3, 6, 7, 12, 14, 13]
        self.assertEqual(res, data)

    def test_deep_post_order(self):
        """Проверка обхода дерева в глубину. Post-order"""
        nodes = self.tree.DeepAllNodes(1)
        res = self.tree.ListNodes(nodes)
        data = [1, 3, 2, 7, 6, 4, 13, 14, 12, 8]
        self.assertEqual(res, data)

    def test_deep_pre_order(self):
        """Проверка обхода дерева в глубину. Pre-order"""
        nodes = self.tree.DeepAllNodes(2)
        res = self.tree.ListNodes(nodes)
        data = [1, 2, 3, 4, 6, 7, 8, 12, 13, 14]
        self.assertEqual(res, data)

if __name__ == "__main__":
    unittest.main()

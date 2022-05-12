"""Модуль содержит тесты для реализации класса Simple Graph"""
import unittest
from main import SimpleTree, SimpleTreeNode

class MainTest(unittest.TestCase):
    def setUp(self):
        self.root = SimpleTreeNode(1, None)
        self.l11 = SimpleTreeNode(2, None)
        self.l12 = SimpleTreeNode(3, None)
        self.l13 = SimpleTreeNode(6, None)
        self.l21 = SimpleTreeNode(5, None)
        self.l22 = SimpleTreeNode(7, None)
        self.l23 = SimpleTreeNode(4, None)
        self.l24 = SimpleTreeNode(8, None)
        self.l31 = SimpleTreeNode(9, None)
        self.l32 = SimpleTreeNode(10, None)
        self.tree = SimpleTree(self.root)
        self.tree.AddChild(self.root, self.l11)
        self.tree.AddChild(self.root, self.l12)
        self.tree.AddChild(self.root, self.l13)
        self.tree.AddChild(self.l11, self.l21)
        self.tree.AddChild(self.l11, self.l22)
        self.tree.AddChild(self.l12, self.l23)
        self.tree.AddChild(self.l13, self.l24)
        self.tree.AddChild(self.l24, self.l31)
        self.tree.AddChild(self.l24, self.l32)

    def test_base(self):
        """Проверка базового дерева"""
        data = self.tree.EvenTrees()
        res = [self.root, self.l12, self.root, self.l13]
        self.assertEqual(res, data)

    def test_empty_result(self):
        """Проверка на возвращение пустого списка"""
        self.tree.DeleteNode(self.l12)
        self.tree.DeleteNode(self.l13)
        data = self.tree.EvenTrees()
        res = []
        self.assertEqual(res, data)

if __name__ == '__main__':
    unittest.main()

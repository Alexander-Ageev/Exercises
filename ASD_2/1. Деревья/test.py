"""Тесты для модуля main.py, в котором реализован тип данных ДЕРЕВЬЯ"""
import unittest
from main import SimpleTreeNode, SimpleTree

class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        """Создание тестового дерева"""
        root = SimpleTreeNode(9, None)
        a = SimpleTreeNode(4, root)
        aa = SimpleTreeNode(3, a)
        ab = SimpleTreeNode(6, a)
        aaa = SimpleTreeNode(5, ab)
        aab = SimpleTreeNode(7, ab)
        b = SimpleTreeNode(17, root)
        bb = SimpleTreeNode(22, b)
        bbb = SimpleTreeNode(20, bb)
        tree = SimpleTree(root)
        tree.AddChild(root, a)
        tree.AddChild(root, b)
        tree.AddChild(a, aa)
        tree.AddChild(a, ab)
        tree.AddChild(ab, aaa)
        tree.AddChild(ab, aab)
        tree.AddChild(b, bb)
        tree.AddChild(bb, bbb)
        self.a = a
        self.aa = aa
        self.ab = ab
        self.aaa = aaa
        self.aab = aab
        self.b = b
        self.bb = bb
        self.bbb = bbb
        self.tree = tree

    def test_init(self):
        """Проверка на корректность создания дерева"""
        nodes = self.tree.GetAllNodes()
        data = self.tree.GetNodesValues(nodes)
        res = [9, 4, 3, 6, 5, 7, 17, 22, 20]
        self.assertEqual(data, res)

    def test_del(self):
        """Проверка на корректность удаления узла"""
        self.tree.DeleteNode(self.a)
        nodes = self.tree.GetAllNodes()
        data = self.tree.GetNodesValues(nodes)
        res = [9, 17, 22, 20]
        self.assertEqual(data, res)

    def test_find_value(self):
        """Проверка на корректность поиска всех узлов по значению"""
        self.aab.node_value = 17
        nodes = self.tree.FindNodesByValue(17) 
        data = self.tree.GetNodesValues(nodes)
        res = [17, 17]
        self.assertEqual(data, res)

    def test_move_node(self):
        """Проверка на корректность переноса ветви"""
        self.tree.MoveNode(self.ab, self.b)
        nodes = self.tree.GetAllNodes()
        data = self.tree.GetNodesValues(nodes)
        res = [9, 4, 3, 17, 22, 20, 6, 5, 7]
        self.assertEqual(data, res)

    def test_counts(self):
        """Проверка на корректность подсчета количества узлов и листьев дерева"""
        nodes = self.tree.Count()
        leaf = self.tree.LeafCount()
        data = [nodes, leaf]
        res = [9, 4]
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()

"""Тесты для модуля main.py, в котором реализован тип данных ДЕРЕВЬЯ"""
import unittest
from main import SimpleTreeNode, SimpleTree

class MainTest(unittest.TestCase):
    def test_init(self):
        """Проверка на корректность создания дерева"""
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
        nodes = tree.GetAllNodes()
        data = tree.GetNodesValues(nodes)
        res = [9, 4, 3, 6, 5, 7, 17, 22, 20]
        self.assertEqual(data, res)

    def test_del(self):
        """Проверка на корректность удаления узла"""
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
        tree.DeleteNode(a)
        nodes = tree.GetAllNodes()
        data = tree.GetNodesValues(nodes)
        res = [9, 17, 22, 20]
        self.assertEqual(data, res)

    def test_find_value(self):
        """Проверка на корректность поиска всех узлов по значению"""
        root = SimpleTreeNode(9, None)
        a = SimpleTreeNode(4, root)
        aa = SimpleTreeNode(3, a)
        ab = SimpleTreeNode(6, a)
        aaa = SimpleTreeNode(5, ab)
        aab = SimpleTreeNode(17, ab)
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
        nodes = tree.FindNodesByValue(17) 
        data = tree.GetNodesValues(nodes)
        res = [17, 17]
        self.assertEqual(data, res)

    def test_move_node(self):
        """Проверка на корректность переноса ветви"""
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
        tree.MoveNode(ab, b)
        nodes = tree.GetAllNodes()
        data = tree.GetNodesValues(nodes)
        res = [9, 4, 3, 17, 22, 20, 6, 5, 7]
        self.assertEqual(data, res)

    def test_counts(self):
        """Проверка на корректность подсчета количества узлов и листьев дерева"""
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
        nodes = tree.Count()
        leaf = tree.LeafCount()
        data = [nodes, leaf]
        res = [9, 4]
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()

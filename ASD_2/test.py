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
        data = tree.GetAllNodesValues()
        res = [9, 4, 3, 6, 5, 7, 17, 22, 20]
        self.assertEqual(data, res)

    def test_del(self):
        

if __name__ == '__main__':
    unittest.main()


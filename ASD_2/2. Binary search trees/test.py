import unittest
from main import BSTNode, BST

ELEMENTS_COUNT = 15
ROOT = 8

class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        """Автоматическая генерация тестового дерева. Проверка метода AddKeyValue"""
        nodes = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        root = BSTNode(ROOT, ROOT, None)
        tree = BST(root)
        for i in nodes:
            tree.AddKeyValue(i, i)
        self.root = root
        self.tree = tree

    def test_tree(self):
        """Проверка структуры тестового дерева"""
        res = []
        for i in range(1, ELEMENTS_COUNT+1):
            node = self.tree.FindNodeByKey(i).Node
            if node.LeftChild is None:
                lChild = None
            else:
                lChild = node.LeftChild.NodeValue
            if node.RightChild is None:
                rChild = None
            else:
                rChild = node.RightChild.NodeValue
            res.append(lChild)
            res.append(rChild)         
        data = [None, None, 1, 3, None, None, 2, 6, None, None, 5, 7, None, None, 4, 12, None, None,
        9, 11, None, None, 10, 14, None, None, 13, 15, None, None]
        #data = [None, None, 1, 3, None, None]
        self.assertEqual(data, res)

    def test_find_exist_key(self):
        """Проверка поиска существующего ключа"""
        res = self.tree.FindNodeByKey(7).Node.Parent.NodeValue
        data = 6
        self.assertEqual(data, res)

    def test_find_add_to_left(self):
        """Проверка поиска для добавления узла слева"""
        node_find = self.tree.FindNodeByKey(-1)
        res = [node_find.Node.NodeValue, node_find.ToLeft]
        data = [1, True]
        self.assertEqual(data, res)

    def test_find_add_to_right(self):
        """Проверка поиска для добавления узла справа"""
        node_find = self.tree.FindNodeByKey(18)
        res = [node_find.Node.NodeValue, node_find.ToLeft]
        data = [15, False]
        self.assertEqual(data, res)
    
    def test_add_exist_key(self):
        """Проверка добавления ключа с существующим значением"""
        res = self.tree.AddKeyValue(7, 7)
        data = False
        self.assertEqual(res, data)

    def test_find_max_root(self):
        """Поиск максимального значения начиная с корня"""
        node = self.tree.FinMinMax(self.root, True)
        res = node.NodeValue
        data = 15
        self.assertEqual(res, data)

    def test_find_min_root(self):
        """Поиск минимального значения начиная с корня"""
        node = self.tree.FinMinMax(self.root, False)
        res = node.NodeValue
        data = 1
        self.assertEqual(res, data)

    def test_find_max_node(self):
        """Поиск максимального значения начиная с NodeValue = 4"""
        node = self.tree.FindNodeByKey(4).Node
        res = self.tree.FinMinMax(node, True).NodeValue
        data = 7
        self.assertEqual(res, data)

    def test_find_min_node(self):
        """Поиск минимального значения начиная с NodeValue = 10"""
        node = self.tree.FindNodeByKey(10).Node
        print(node.LeftChild)
        res = self.tree.FinMinMax(node, False).NodeValue
        data = 9
        self.assertEqual(res, data)

if __name__ == "__main__":
    unittest.main()
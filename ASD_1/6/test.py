import unittest
from main import OrderedList, Node

class main_tests(unittest.TestCase):
    def test_compare_less(self):
        l = OrderedList(True)
        n1 = Node(1)
        n2 = Node(2)
        data = l.compare(n1, n2)
        res =  -1
        self.assertEqual( data, res)
    
    def test_compare_equal(self):
        l = OrderedList(True)
        n1 = Node(1)
        n2 = Node(1)
        data = l.compare(n1, n2)
        res =  0
        self.assertEqual( data, res)

    def test_compare_more(self):
        l = OrderedList(True)
        n1 = Node(3)
        n2 = Node(2)
        data = l.compare(n1, n2)
        res =  1
        self.assertEqual( data, res)

    def test_add_in_void(self):
        l = OrderedList(True)
        n1 = Node(3)
        l.add(n1)
        data = l.get_all()
        res =  [n1]
        self.assertEqual( data, res)

    def test_add_in_head(self):
        l = OrderedList(True)
        n1 = Node(3)
        n2 = Node(2)
        l.add(n1)
        l.add(n2)
        data = l.get_all()
        res =  [n2, n1]
        self.assertEqual( data, res)


if __name__ == '__main__':
    unittest.main()
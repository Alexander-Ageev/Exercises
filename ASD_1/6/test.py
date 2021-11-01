import unittest, random
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
        data = l.get_head_tail() + l.get_all()
        res =  [n1, None, n1]
        self.assertEqual( data, res)

    def test_add_in_head_up(self):
        l = OrderedList(True)
        n1 = Node(3)
        n2 = Node(2)
        l.add(n1)
        l.add(n2)
        data = l.get_head_tail() + l.get_all()
        res =  [n2, n1, n2, n1]
        self.assertEqual( data, res)

    def test_add_in_head_down(self):
        l = OrderedList(False)
        n1 = Node(3)
        n2 = Node(2)
        l.add(n1)
        l.add(n2)
        data = l.get_head_tail() + l.get_all()
        res =  [n1, n2, n1, n2]
        self.assertEqual( data, res)

    def test_add_in_tail_up(self):
        l = OrderedList(True)
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_all()
        res =  [n1, n3, n1, n2, n3]
        self.assertEqual( data, res)

    def test_add_in_tail_down(self):
        l = OrderedList(False)
        n1 = Node(3)
        n2 = Node(2)
        n3 = Node(1)
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_all()
        res =  [n1, n3, n1, n2, n3]
        self.assertEqual( data, res)


    def test_add_in_middle_up(self):
        l = OrderedList(True)
        n1 = Node(1)
        n2 = Node(3)
        n3 = Node(2)
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_all()
        res =  [n1, n2, n1, n3, n2]
        self.assertEqual( data, res)

    def test_add_in_middle_down(self):
        l = OrderedList(False)
        n1 = Node(3)
        n2 = Node(1)
        n3 = Node(2)
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_all()
        res =  [n1, n2, n1, n3, n2]
        self.assertEqual( data, res)

    def test_random_down(self):
        for i in range(1000):
            node_count = random.randint(1, 10)
            res_list = []
            l = OrderedList(True)
            for node in range(node_count):
                item = random.randint(0, 100)
                res_list.append(item)
                l.add(Node(item))
            data = l.get_list()
            res = sorted(res_list)
            self.assertEqual( data, res)

    def test_random_up(self):
        for i in range(1000):
            node_count = random.randint(1, 10)
            res_list = []
            l = OrderedList(False)
            for node in range(node_count):
                item = random.randint(0, 100)
                res_list.append(item)
                l.add(Node(item))
            data = l.get_list()
            res = sorted(res_list, reverse=True)
            self.assertEqual( data, res)



if __name__ == '__main__':
    unittest.main()
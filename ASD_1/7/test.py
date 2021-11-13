import unittest, random
from main import OrderedList, Node, OrderedStringList, OrderedStringList

class main_tests(unittest.TestCase):
    def test_compare_less(self):
        l = OrderedList(True)
        n1 = 1
        n2 = 2
        data = l.compare(n1, n2)
        res =  -1
        self.assertEqual( data, res)
    
    def test_compare_equal(self):
        l = OrderedList(True)
        n1 = 1
        n2 = 1
        data = l.compare(n1, n2)
        res =  0
        self.assertEqual( data, res)

    def test_compare_more(self):
        l = OrderedList(True)
        n1 = 3
        n2 = 2
        data = l.compare(n1, n2)
        res =  1
        self.assertEqual( data, res)

    def test_add_in_void(self):
        l = OrderedList(True)
        n1 = 3
        l.add(n1)
        data = l.get_head_tail() + l.get_list()
        res =  [n1, n1, n1]
        self.assertEqual( data, res)

    def test_add_in_head_up(self):
        l = OrderedList(True)
        n1 = 3
        n2 = 2
        l.add(n1)
        l.add(n2)
        data = l.get_head_tail() + l.get_list()
        res =  [n2, n1, n2, n1]
        self.assertEqual( data, res)

    def test_add_in_head_down(self):
        l = OrderedList(False)
        n1 = 3
        n2 = 2
        l.add(n1)
        l.add(n2)
        data = l.get_head_tail() + l.get_list()
        res =  [n1, n2, n1, n2]
        self.assertEqual( data, res)

    def test_add_up(self):
        l = OrderedList(True)
        n1 = 1
        n2 = 2
        n3 = 3
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_list()
        res =  [n1, n3, n1, n2, n3]
        self.assertEqual( data, res)

    def test_add_down(self):
        l = OrderedList(False)
        n1 = 3
        n2 = 2
        n3 = 1
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_list()
        res =  [n1, n3, n1, n2, n3]
        self.assertEqual( data, res)


    def test_add_in_middle_up(self):
        l = OrderedList(True)
        n1 = 1
        n2 = 3
        n3 = 2
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_list()
        res =  [n1, n2, n1, n3, n2]
        self.assertEqual( data, res)

    def test_add_in_middle_down(self):
        l = OrderedList(False)
        n1 = 3
        n2 = 1
        n3 = 2
        l.add(n1)
        l.add(n2)
        l.add(n3)
        data = l.get_head_tail() + l.get_list()
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
                l.add(item)
            data = l.get_head_tail() + l.get_list()
            header = [min(res_list), max(res_list)]
            res = header + sorted(res_list)
            self.assertEqual( data, res)

    def test_random_up(self):
        for i in range(1000):
            node_count = random.randint(1, 10)
            res_list = []
            l = OrderedList(False)
            for node in range(node_count):
                item = random.randint(0, 100)
                res_list.append(item)
                l.add(item)
            data = l.get_head_tail() + l.get_list()
            header = [max(res_list), min(res_list)]
            res = header + sorted(res_list, reverse = True)
            self.assertEqual( data, res)

    def test_compare_string_less(self):
        l = OrderedStringList(True)
        n1 = 'abb '
        n2 = ' abc'
        data = l.compare(n1, n2)
        res =  -1
        self.assertEqual( data, res)
    
    def test_compare_string_equal(self):
        l = OrderedStringList(True)
        n1 = 'abb'
        n2 = ' abb'
        data = l.compare(n1, n2)
        res =  0
        self.assertEqual( data, res)

    def test_compare_string_more(self):
        l = OrderedStringList(True)
        n1 = ' abc'
        n2 = 'abb '
        data = l.compare(n1, n2)
        res =  1
        self.assertEqual( data, res)

# Delete tests
    def test_del_one_from_one_up(self):
        n1 = 3
        ls = OrderedList(True)
        ls.add(n1)
        ls.delete(n1)
        data = ls.get_head_tail() + ls.get_list()
        res = [None, None]
        self.assertEqual(data, res)  

    def test_del_one_from_one_down(self):
        n1 = 3
        ls = OrderedList(False)
        ls.add(n1)
        ls.delete(n1)
        data = ls.get_head_tail() + ls.get_list()
        res = [None, None]
        self.assertEqual(data, res)  

    def test_del_none_from_one_up(self):
        n1 = 3
        ls = OrderedList(True)
        ls.add(n1)
        ls.delete(1)
        data = ls.get_head_tail() + ls.get_list()
        res = [n1, n1, n1]
        self.assertEqual(data, res)  

    def test_del_none_from_one_down(self):
        n1 = 3
        ls = OrderedList(False)
        ls.add(n1)
        ls.delete(1)
        data = ls.get_head_tail() + ls.get_list()
        res = [n1, n1, n1]
        self.assertEqual(data, res)  

    def test_del_one_first_from_many_up(self):
        n1 = 2
        n2 = 1
        n3 = 3        
        ls = OrderedList(True)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        ls.delete(n2)
        data = ls.get_head_tail() + ls.get_list()
        res = [n1, n3, n1, n3]
        self.assertEqual(data, res)  

    def test_del_one_first_from_many_down(self):
        n1 = 2
        n2 = 1
        n3 = 3        
        ls = OrderedList(False)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        ls.delete(n2)
        data = ls.get_head_tail() + ls.get_list()
        res = [n3, n1, n3, n1]
        self.assertEqual(data, res)  

def test_del_one_middle_from_many_up(self):
        n1 = 2
        n2 = 2
        n3 = 3        
        ls = OrderedList(False)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        print(ls.get_all())
        ls.delete(n2)
        print(ls.get_all())
        data = ls.get_head_tail() + ls.get_list()
        res = [n2, n3, n2, n3]
        #res = [n3, n3, 3]
        self.assertEqual(data, res)  


    def test_del_one_middle_from_many_down(self):
        n1 = 2
        n2 = 2
        n3 = 3        
        ls = OrderedList(False)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        print(ls.get_all())
        ls.delete(n2)
        print(ls.get_all())
        data = ls.get_head_tail() + ls.get_list()
        res = [n3, n2, n3, n2]
        #res = [n3, n3, 3]
        self.assertEqual(data, res)  


"""
    def test_del_one_last_from_many(self):
        n1 = 1
        n2 = 2
        n3 = 3        
        ls = OrderedList(True)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        ls.delete(3)
        data = ls.get_head_tail() + ls.get_list()
        res = [n1, n2, 1, 2]
        self.assertEqual(data, res)

    def test_random_del_up(self):
        for t in range(1000):
            ls = OrderedList(True)
            node_count = random.randint(0, 10)
            l = []
            for i in range(node_count):
                node = random.randint(-100, 100)
                ls.add(node)
                l.append(node)
            l = sorted(l)
            del_node = random.randint(-100, 100)
            ls.delete(del_node)
            data = data = ls.get_head_tail() + ls.get_list()
            try:
                l.remove(del_node)
            except:
                pass
            if l:
                res = [l[0], l[-1]] + l
            else:
                res = [None, None]
            self.assertEqual(data, res)

    def test_random_del_down(self): # не работает с удалением всех элементов
        for t in range(1000):
            ls = OrderedList(False)
            node_count = random.randint(0, 10)
            l = []
            for i in range(node_count):
                node = random.randint(-100, 100)
                ls.add(node)
                l.append(node)
            l = sorted(l, reverse=True)
            del_node = random.randint(-100, 100)
            ls.delete(del_node)
            data = data = ls.get_head_tail() + ls.get_list()
            try:
                l.remove(del_node)
            except:
                pass
            if l:
                res = [l[0], l[-1]] + l
            else:
                res = [None, None]
            self.assertEqual(data, res)

#########################################################################

    def test_len_void(self):
        ls = OrderedList(True)
        data = ls.len()
        res = 0
        self.assertEqual(data, res)  

    def test_len_random(self):
        for t in range(1000):
            nodes_count = random.randint(0, 10)
            ls = OrderedList(True)
            for i in range(nodes_count):
                ls.add(random.randint(0, 10))
            data = ls.len()
            res = nodes_count
            self.assertEqual(data, res)  

    def test_clean(self):
        n1 = 2
        n2 = 2
        n3 = 3        
        ls = OrderedList(False)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        ls.clean(True)
        data = ls.get_head_tail() + ls.get_list()
        res = [None, None]
        self.assertEqual(data, res)

    def test_find_none(self):
        n1 = 2
        n2 = 2
        n3 = 3        
        ls = OrderedList(False)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        data = ls.find(1)
        res = None
        self.assertEqual(data, res)

    def test_find_first(self):
        n1 = 2
        n2 = 2
        n3 = 3        
        ls = OrderedList(False)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        data = ls.find(3)
        res = ls.get_index(0)
        self.assertEqual(data, res)

    def test_find_first_1(self):
        n1 = 2
        n2 = 2
        n3 = 3        
        ls = OrderedList(True)
        ls.add(n1)
        ls.add(n2)
        ls.add(n3)
        data = ls.find(2)
        res = ls.get_index(0)
        self.assertEqual(data, res)

    def test_find_random(self):
        for t in range(1000):
            l = []
            nodes_count = random.randint(0, 10)
            ls = OrderedList(True)
            for i in range(nodes_count):
                r = random.randint(0, 10)
                ls.add(r)
                l.append(r)
            l = sorted(l)
            data = ls.find(5) 
            try:
                res = ls.get_index(l.index(5))
            except:
                res = None
            self.assertEqual(data, res)  

"""


if __name__ == '__main__':
    unittest.main()
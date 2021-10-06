import unittest
from main import Node, LinkedList2

class main_tests(unittest.TestCase):
    def test_find_one_in_one(self):
        n1 = Node(1)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        data = ls.find(1)
        res = n1
        self.assertEqual(data, res)

    def test_find_one_in_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        data = ls.find(2)
        res = n2
        self.assertEqual(data, res)  

    def test_find_one_in_dublicate(self):
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(3)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        data = ls.find(1)
        res = n1
        self.assertEqual(data, res)  

    def test_find_one_in_void(self):
        ls = LinkedList2()
        data = ls.find(1)
        res = None
        self.assertEqual(data, res)  

    def test_find_void_in_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        data = ls.find(4)
        res = None
        self.assertEqual(data, res)  

    def test_find_many_in_one(self):
        n1 = Node(1)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        data = ls.find_all(1)
        res = [n1]
        self.assertEqual(data, res)  

    def test_find_many_in_many(self):
        n1 = Node(3)
        n2 = Node(3)
        n3 = Node(3)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        data = ls.find_all(3)
        res = [n1, n2, n3]
        self.assertEqual(data, res)  

    def test_find_many_in_void(self):
        ls = LinkedList2()
        data = ls.find_all(1)
        res = []
        self.assertEqual(data, res)  

    def test_del_one_from_one(self):
        n1 = Node(3)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.delete(3, False)
        data = ls.get_head_tail() + ls.list_node()
        res = [None, None]
        self.assertEqual(data, res)  

    def test_del_none_from_one(self):
        n1 = Node(3)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.delete(1, False)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n1, 3]
        self.assertEqual(data, res)  

    def test_del_one_first_from_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(1, False)
        data = ls.get_head_tail() + ls.list_node()
        res = [n2, n3, 2, 3]
        self.assertEqual(data, res)  

    def test_del_one_middle_from_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(2, False)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n3, 1, 3]
        self.assertEqual(data, res)  

    def test_del_one_last_from_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(3, False)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n2, 1, 2]
        self.assertEqual(data, res)  

    def test_del_all_from_many(self):
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(1)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(1, True)
        data = ls.get_head_tail() + ls.list_node()
        res = [None, None]
        self.assertEqual(data, res) 

    def test_del_two_first_from_many(self):
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(1, True)
        data = ls.get_head_tail() + ls.list_node()
        res = [n3, n3, 3]
        self.assertEqual(data, res) 

    def test_del_two_last_from_many(self):
        n1 = Node(1)
        n2 = Node(3)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(3, True)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n1, 1]
        self.assertEqual(data, res)

    def test_del_two_side_from_many(self):
        n1 = Node(3)
        n2 = Node(1)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(3, True)
        data = ls.get_head_tail() + ls.list_node()
        res = [n2, n2, 1]
        self.assertEqual(data, res) 

    def test_del_first_from_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(1, True)
        data = ls.get_head_tail() + ls.list_node()
        res = [n2, n3, 2, 3]
        self.assertEqual(data, res)  

    def test_del_middle_from_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(2, True)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n3, 1, 3]
        self.assertEqual(data, res)  

    def test_del_last_from_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.delete(3, True)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n2, 1, 2]
        self.assertEqual(data, res)  

    def test_clean(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.clean()
        data = ls.get_head_tail() + ls.list_node()
        res = [None, None]
        self.assertEqual(data, res) 

    def test_clean_void(self):     
        ls = LinkedList2()
        ls.clean()
        data = ls.get_head_tail() + ls.list_node()
        res = [None, None]
        self.assertEqual(data, res) 

    def test_len_0(self): 
        ls = LinkedList2()
        data =ls.len()
        res = 0
        self.assertEqual(data, res) 

    def test_len_3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)        
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3) 
        data =ls.len()
        res = 3
        self.assertEqual(data, res) 

    def test_add_in_head_void(self):
        n1 = Node(1)
        ls = LinkedList2()
        ls.add_in_head(n1)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n1, 1]
        self.assertEqual(data, res)  

    def test_add_in_head_many(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(0)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3) 
        ls.add_in_head(n4)
        data = ls.get_head_tail() + ls.list_node()
        res = [n4, n3, 0, 1, 2, 3]
        self.assertEqual(data, res)  

    def test_insert_in_head(self):
        n1 = Node(1)
        ls = LinkedList2()
        ls.insert(None, n1)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n1, 1]
        self.assertEqual(data, res) 

    def test_insert_in_head_error(self):
        n1 = Node(1)
        n2 = Node(1)
        ls = LinkedList2()
        ls.insert(n2, n1)
        data = ls.get_head_tail() + ls.list_node()
        res = [None, None]
        self.assertEqual(data, res) 

    def test_insert_in_tail(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(0)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.insert(None, n4)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n4, 1, 2, 3, 0]
        self.assertEqual(data, res) 

    def test_insert_in_list(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(0)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.insert(n1, n4)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n3, 1, 0, 2, 3]
        self.assertEqual(data, res)

    def test_insert_after_tail(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(0)
        ls = LinkedList2()
        ls.add_in_tail(n1)
        ls.add_in_tail(n2)
        ls.add_in_tail(n3)
        ls.insert(n3, n4)
        data = ls.get_head_tail() + ls.list_node()
        res = [n1, n4, 1, 2, 3, 0]
        self.assertEqual(data, res) 

if __name__ == '__main__':
    unittest.main()
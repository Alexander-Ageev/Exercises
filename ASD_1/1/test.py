import unittest
from main import Node, LinkedList


class main_tests(unittest.TestCase):
    def test_del_one_first_3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.delete(1)
        data = s_list.list_all_nodes()    
        res = [2, 3]
        self.assertEqual( data , res)

    def test_del_one_middle_3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.delete(2)
        data = s_list.list_all_nodes()    
        res = [1, 3]
        self.assertEqual( data , res)

    def test_del_one_last_3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.delete(3)
        data = s_list.list_all_nodes()    
        res = [1, 2]
        self.assertEqual( data , res)

    def test_del_one_first_1(self):
        n1 = Node(1)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.delete(1)
        data = s_list.list_all_nodes()    
        res = []
        self.assertEqual( data , res)

    def test_del_one_first_2(self):
        n1 = Node(1)
        n2 = Node(2)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.delete(1)
        data = s_list.list_all_nodes()    
        res = [2]
        self.assertEqual( data , res)

    def test_del_one_last_2(self):
        n1 = Node(1)
        n2 = Node(2)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.delete(2)
        data = s_list.list_all_nodes()    
        res = [1]
        self.assertEqual( data , res)

    def test_del_one_void(self):
        s_list = LinkedList()
        s_list.delete(1)
        data = s_list.list_all_nodes()    
        res = []
        self.assertEqual( data , res)

    def test_del_one_void_all(self):
        s_list = LinkedList()
        s_list.delete(1, True)
        data = s_list.list_all_nodes()    
        res = []
        self.assertEqual( data , res)

    def test_del_one_first_1_all(self):
        n1 = Node(1)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.delete(1, True)
        data = s_list.list_all_nodes()    
        res = []
        self.assertEqual( data , res)
    
    def test_del_one_last_3_all(self):
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.delete(1, True)
        data = s_list.list_all_nodes()    
        res = [3]
        self.assertEqual( data , res)


    def test_del_one_last_3_all(self):
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.delete(4, True)
        data = s_list.list_all_nodes()    
        res = [1, 1, 3]
        self.assertEqual( data , res)

    def test_clean_full(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.clean()
        data = s_list.list_all_nodes()    
        res = []
        self.assertEqual( data , res)

    def test_clean_one(self):
        n1 = Node(1)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.clean()
        data = s_list.list_all_nodes()    
        res = []
        self.assertEqual( data , res)

    def test_clean_void(self):
        s_list = LinkedList()
        s_list.clean()
        data = s_list.list_all_nodes()    
        res = []
        self.assertEqual( data , res)

    def test_find_all_full(self):
        n1 = Node(1)
        n2 = Node(3)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        data = s_list.find_all(3)
        res = [n2, n3]
        self.assertEqual( data , res)

    def test_find_all_void(self):
        s_list = LinkedList()
        data = s_list.find_all(3)
        res = []
        self.assertEqual( data , res)

    def test_find_all_no_element(self):
        n1 = Node(1)
        n2 = Node(3)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        data = s_list.find_all(2)
        res = []
        self.assertEqual( data , res)

    def test_len_0(self):
        s_list = LinkedList()
        data = s_list.len()
        res = 0
        self.assertEqual( data , res)

    def test_len_1(self):
        n1 = Node(1)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        data = s_list.len()
        res = 1
        self.assertEqual( data , res)

    def test_len_3(self):
        n1 = Node(1)
        n2 = Node(3)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        data = s_list.len()
        res = 3
        self.assertEqual( data , res)

    def test_insert_void(self):
        n1 = Node(1)
        s_list = LinkedList()
        s_list.insert(None, n1)
        data = s_list.list_all_nodes()
        res = [1]
        self.assertEqual( data , res)

    def test_insert_start(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n3)
        s_list.insert(None, n2)
        data = s_list.list_all_nodes()
        res = [2, 1, 3]
        self.assertEqual( data , res)

    def test_insert_middle(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n3)
        s_list.insert(n1, n2)
        data = s_list.list_all_nodes()
        res = [1, 2, 3]
        self.assertEqual( data , res)

    def test_insert_end(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.insert(n2, n3)
        data = s_list.list_all_nodes()
        res = [1, 2, 3]
        self.assertEqual( data , res)

    def test_insert_nowhere(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.insert(n4, n3)
        data = s_list.list_all_nodes()
        res = [1, 2]
        self.assertEqual( data , res)

if __name__ == '__main__':
    unittest.main()
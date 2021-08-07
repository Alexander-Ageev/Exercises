import unittest
from main import get_unsorted_index, Football, check_sequence

class main_tests(unittest.TestCase):
    def test_get_unsorted_index_simple(self):
        data = [1, 2, 4, 3, 5]
        res =  [2, 3]
        self.assertEqual(get_unsorted_index(data), res)
    def test_get_unsorted_index_advance(self):
        data = [1, 3, 8, 6, 5]
        res =  [2, 4]
        self.assertEqual(get_unsorted_index(data), res)
    def test_get_unsorted_index_reverse(self):
        data = [1, 5, 4, 3, 2]
        res =  [1, 2, 3, 4]
        self.assertEqual(get_unsorted_index(data), res)

    def test_check_sequence_1(self):
        data = [1, 2, 3]
        res = True
        self.assertEqual(check_sequence(data), res)
    def test_check_sequence_2(self):
        data = [1, 2, 4]
        res = False
        self.assertEqual(check_sequence(data), res)
    def test_check_sequence_1(self):
        data = [0, 2, 3, 4, 5]
        res = False
        self.assertEqual(check_sequence(data), res)

    def test_Football_basic_1(self):
        data = [1, 3, 2]
        res = True
        self.assertEqual(Football(data, len(data)), res)        
    def test_Football_basic_2(self):
        data = [3, 2, 1]
        res = True
        self.assertEqual(Football(data, len(data)), res) 
    def test_Football_basic_3(self):
        data = [1, 7, 5, 3, 9]
        res = True
        self.assertEqual(Football(data, len(data)), res) 
    def test_Football_basic_4(self):
        data = [9, 5, 3, 7, 1]
        res = False
        self.assertEqual(Football(data, len(data)), res) 
    def test_Football_basic_5(self):
        data = [1, 4, 3, 2, 5]
        res = True
        self.assertEqual(Football(data, len(data)), res) 
    def test_Football_basic_6(self):
        data = [1, 2, 3]
        res = False
        self.assertEqual(Football(data, len(data)), res) 
    def test_Football_basic_7(self):
        data = [1, 8, 7, 6, 5, 9]
        res = True
        self.assertEqual(Football(data, len(data)), res) 
if __name__ == '__main__':
    unittest.main()
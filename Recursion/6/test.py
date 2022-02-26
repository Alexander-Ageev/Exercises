import unittest
import random as rnd
from main import print_even_idx

class MainTest(unittest.TestCase):
    def test_null(self):
        """Test null data"""
        data = []
        res = []
        self.assertCountEqual(print_even_idx(data), res)

    def test_odd_data(self):
        """Test simple data"""
        data = [1, 2]
        res = [1]
        self.assertCountEqual(print_even_idx(data), res)

    def test_data(self):
        """Test simple data"""
        data = [1, 2, 3]
        res = [1, 3]
        self.assertCountEqual(print_even_idx(data), res)

    def test_random(self):
        """Test by random"""
        elements_num = rnd.randint(0, 100)
        data = []
        res = []
        for i in range(elements_num):
            element = rnd.randint(0, 10)
            data.append(element)
            if i % 2 == 0:
                res.append(element)
        self.assertCountEqual(print_even_idx(data), res)

if __name__ == '__main__':
    unittest.main()

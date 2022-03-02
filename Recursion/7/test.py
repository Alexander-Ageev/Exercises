import unittest
import random as rnd
from main import rec_max_search, max_search

class MainTest(unittest.TestCase):
    def test_shuffle_data(self):
        """Test by simple shuffle array"""
        data = [-9, -9, -5, -5, -4, -3, -1, 9]
        res = 5
        self.assertEqual(rec_max_search(data), max_search(data), res)

    def test_duplicate_data(self):
        """Test by shuffle array with diplicate"""
        data = [1, 7, 7, 5, 2]
        res = 7
        self.assertEqual(rec_max_search(data), max_search(data), res)

    def test_null(self):
        """Test by empty array"""
        data = []
        res = None
        self.assertEqual(rec_max_search(data), max_search(data), res)

    def test_one(self):
        """Test by one value array"""
        data = [1]
        res = None
        self.assertEqual(rec_max_search(data), max_search(data), res)

    def test_random(self):
        """Test by random value array"""
        for epoch in range(10000):
            array_size = rnd.randint(0, 10)
            data = [rnd.randint(-10, 10)  for i in range(array_size)]
            res_data = data.copy()
            if array_size >= 2:
                res_data.sort()
                res = res_data[-2]
            else:
                res = None
            self.assertEqual(rec_max_search(data), max_search(data), res)

if __name__ == '__main__':
    unittest.main()

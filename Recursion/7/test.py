import unittest
from main import linear_max_search

class MainTest(unittest.TestCase):
    def test_shuffle_data(self):
        """Test by simple shuffle array"""
        data = [1, 3, 7, 5, 2]
        res = 5
        self.assertEqual(linear_max_search(data), res)

    def test_duplicate_data(self):
        """Test by shuffle array with diplicate"""
        data = [1, 7, 7, 5, 2]
        res = 7
        self.assertEqual(linear_max_search(data), res)

    def test_null(self):
        """Test by empty array"""
        data = []
        res = None
        self.assertEqual(linear_max_search(data), res)

    def test_one(self):
        """Test by one value array"""
        data = [1]
        res = None
        self.assertEqual(linear_max_search(data), res)

if __name__ == '__main__':
    unittest.main()

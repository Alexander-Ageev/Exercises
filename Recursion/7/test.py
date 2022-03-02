import unittest
from main import linear_max_search, sort_max_search

class MainTest(unittest.TestCase):
    def test_loop_shuffle_data(self):
        """Test by simple shuffle array"""
        data = [1, 3, 7, 5, 2]
        res = 5
        self.assertEqual(linear_max_search(data), res)

    def test_loop_duplicate_data(self):
        """Test by shuffle array with diplicate"""
        data = [1, 7, 7, 5, 2]
        res = 7
        self.assertEqual(linear_max_search(data), res)

    def test_loop_null(self):
        """Test by empty array"""
        data = []
        res = None
        self.assertEqual(linear_max_search(data), res)

    def test_loop_one(self):
        """Test by one value array"""
        data = [1]
        res = None
        self.assertEqual(linear_max_search(data), res)

    def test_sort_shuffle_data(self):
        """Test by simple shuffle array"""
        data = [1, 3, 7, 5, 2]
        res = 5
        self.assertEqual(sort_max_search(data), res)

    def test_sort_duplicate_data(self):
        """Test by shuffle array with diplicate"""
        data = [1, 7, 7, 5, 2]
        res = 7
        self.assertEqual(sort_max_search(data), res)

    def test_sort_null(self):
        """Test by empty array"""
        data = []
        res = None
        self.assertEqual(sort_max_search(data), res)

    def test_sort_one(self):
        """Test by one value array"""
        data = [1]
        res = None
        self.assertEqual(sort_max_search(data), res)

    def test_clear_shuffle_data(self):
        """Test by simple shuffle array"""
        data = [1, 3, 7, 5, 2]
        res = 5
        self.assertEqual(sort_max_search(data), res)

    def test_clear_duplicate_data(self):
        """Test by shuffle array with diplicate"""
        data = [1, 7, 7, 5, 2]
        res = 7
        self.assertEqual(sort_max_search(data), res)

    def test_clear_null(self):
        """Test by empty array"""
        data = []
        res = None
        self.assertEqual(sort_max_search(data), res)

    def test_clear_one(self):
        """Test by one value array"""
        data = [1]
        res = None
        self.assertEqual(sort_max_search(data), res)

if __name__ == '__main__':
    unittest.main()

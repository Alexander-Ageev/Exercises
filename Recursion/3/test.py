import unittest
from main import get_len

class MainTest(unittest.TestCase):
    def test_simple_list(self):
        """Test list with many elements"""
        data = [1, 2, 3, 4]
        res = len(data)
        self.assertEqual(get_len(data), res)

    def test_one_element_list(self):
        """Test list with one element"""
        data = [1]
        res = len(data)
        self.assertEqual(get_len(data), res)

    def test_empty_list(self):
        """Test list without elements"""
        data = []
        res = len(data)
        self.assertEqual(get_len(data), res)

if __name__ == '__main__':
    unittest.main()

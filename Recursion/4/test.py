import unittest
from main import check_palindrom

class MainTest(unittest.TestCase):
    def test_true_odd(self):
        """Test True result for odd-length string"""
        data = 'asdfdsa'
        res = True
        self.assertEqual(check_palindrom(data), res)

    def test_true_even(self):
        """Test True result for even-length string"""
        data = 'asdffdsa'
        res = True
        self.assertEqual(check_palindrom(data), res)

    def test_false_odd(self):
        """Test False result for odd-length string"""
        data = 'asdfdsb'
        res = False
        self.assertEqual(check_palindrom(data), res)

    def test_false_even(self):
        """Test False result for even-length string"""
        data = 'asdfgdsa'
        res = False
        self.assertEqual(check_palindrom(data), res)

    def test_empty_string(self):
        """Test True result for empty string"""
        data = ''
        res = True
        self.assertEqual(check_palindrom(data), res)

    def test_one_char_string(self):
        """Test True result for one-char string"""
        data = 'q'
        res = True
        self.assertEqual(check_palindrom(data), res)

if __name__ == '__main__':
    unittest.main()
    
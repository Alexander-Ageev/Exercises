import unittest
from main import brackets_comb

class MainTest(unittest.TestCase):
    def test_2(self):
        """Test by two brackets"""
        data = '(('
        res = ['()()', '(())']
        self.assertEqual(brackets_comb(data), res)

    def test_1(self):
        """Test by one bracket"""
        data = '('
        res = ['()']
        self.assertEqual(brackets_comb(data), res)

    def test_3(self):
        """Test by three brackets"""
        data = '((('
        res = ['()()()', '()(())', '(())()', '(()())', '((()))']
        self.assertEqual(brackets_comb(data), res)

if __name__ == '__main__':
    unittest.main()

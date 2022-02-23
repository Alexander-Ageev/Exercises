import unittest
import random
from main import print_even_value

class MainTest(unittest.TestCase):
    def test_mixed_data(self):
        """Test by mixed data"""
        data = [1, 2, 3, 4, 5]
        res = [2, 4]
        self.assertEqual(print_even_value(data), res)

    def test_odd_data(self):
        """Test for null result"""
        data = [1, 3, 5]
        res = []
        self.assertEqual(print_even_value(data), res)

    def test_even_data(self):
        """Test for source result"""
        data = [2, 4, 6]
        res = [2, 4, 6]
        self.assertEqual(print_even_value(data), res)

    def test_null_data(self):
        """Test by null source"""
        data = []
        res = []
        self.assertEqual(print_even_value(data), res)

    def test_random(self):
        """Test with random values"""
        data = []
        res = []
        for _ in range(100):
            value = random.randint(0, 9)
            data.append(value)
            if value % 2 == 0:
                res.append(value)
        self.assertEqual(print_even_value(data), res)

if __name__ == '__main__':
    unittest.main()

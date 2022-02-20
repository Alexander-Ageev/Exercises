import unittest
from main import power

class MainTests(unittest.TestCase):
    def test_positive_power(self):
        """Test for a positive degree"""
        number = 2
        degree = 7
        data = power(number, degree)
        res = number**degree
        self.assertEqual( data, res)

    def test_null_power(self):
        """Test for a null degree"""
        number = 2
        degree = 0
        data = power(number, degree)
        res = number**degree
        self.assertEqual( data, res)

    def test_negative_power(self):
        """Test for a negative degree"""
        number = 2
        degree = -5
        data = power(number, degree)
        res = number**degree
        self.assertEqual( data, res)

if __name__ == '__main__':
    unittest.main()

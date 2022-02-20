import unittest
from main import power

class main_tests(unittest.TestCase):
    def test_positive_power(self):
        n = 2
        m = 7
        data = power(n, m)
        res = n**m
        self.assertEqual( data, res)

    def test_null_power(self):
        n = 2
        m = 0
        data = power(n, m)
        res = n**m
        self.assertEqual( data, res)

    def test_negative_power(self):
        n = 2
        m = -5
        data = power(n, m)
        res = n**m
        self.assertEqual( data, res)

if __name__ == '__main__':  
    unittest.main()
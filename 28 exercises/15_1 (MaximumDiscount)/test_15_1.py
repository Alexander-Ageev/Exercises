import unittest
import random
from main import MaximumDiscount

class main_tests(unittest.TestCase):
    def test_basic(self):
        prices = [400, 350, 300, 250, 200, 150, 100]
        res = 450
        self.assertEqual( MaximumDiscount(len(prices), prices), res )
    def test_none_discount(self):
        prices = [400, 350]
        res = 0
        self.assertEqual( MaximumDiscount(len(prices), prices), res )

if __name__ == '__main__':
    unittest.main()
import unittest
from main import dig_sum

class MainTest(unittest.TestCase):
    def test_big_number(self):
        """Big number test"""
        number = 123456789
        res = 45
        self.assertEqual(dig_sum(number), res)

    def test_small_number(self):
        """Test only else case"""
        number = 7
        res = 7
        self.assertEqual(dig_sum(number), res)

    def test_big_negative_number(self):
        """Negative number test"""
        number = -123456789
        res = 45
        self.assertEqual(dig_sum(number), res)

    def test_small_negative_number(self):
        """Test only else case"""
        number = -1
        res = 1
        self.assertEqual(dig_sum(number), res)

    def test_null(self):
        """Test null number"""
        number = 0
        res = 0
        self.assertEqual(dig_sum(number), res)

    def test_boundary_value(self):
        """Test boundary value"""
        number = -1000
        res = 1
        self.assertEqual(dig_sum(number), res)

if __name__ == '__main__':
    unittest.main()

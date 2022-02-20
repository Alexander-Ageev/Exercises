import unittest
from main import dig_sum, get_len, get_digit

class MainTest(unittest.TestCase):
    def test_get_len_basic(self):
        """Length = 3"""
        number = 123
        res = 3
        self.assertEqual(get_len(number), res)
    def test_get_len_one(self):
        """Length = 1"""
        number = 1
        res = 1
        self.assertEqual(get_len(number), res)

    def test_get_digit(self):
        """Return 4"""
        number = 121
        res = 4
        self.assertEqual(get_digit(number, get_len(number)), res)

    def test_base_positive(self):
        """Basic positive test"""
        number = 123456789
        res = 45
        self.assertEqual( dig_sum(number), res)

    def test_base_negative(self):
        """Basic negative test"""
        number = -123456789
        res = 45
        self.assertEqual( dig_sum(number), res)

    def test_boundary_value(self):
        """Test boundary value"""
        number = -1000
        res = 1
        self.assertEqual( dig_sum(number), res)

if __name__ == '__main__':
    unittest.main()

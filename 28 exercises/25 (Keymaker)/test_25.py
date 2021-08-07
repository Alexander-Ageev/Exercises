import unittest
from main import Keymaker

class main_tests(unittest.TestCase):
    def test_10(self):
        data = 10
        res =  '1001000010'
        self.assertEqual(Keymaker(data), res)
    def test_1(self):
        data = 1
        res =  '1'
        self.assertEqual(Keymaker(data), res)
if __name__ == '__main__':
    unittest.main()
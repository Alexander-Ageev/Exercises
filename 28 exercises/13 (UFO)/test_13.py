import unittest
from main import UFO

class main_tests(unittest.TestCase):
    def test_octo(self):
        data = [1234, 1777]
        res = [668, 1023]
        self.assertEqual(UFO(len(data), data, True), res)
    def test_hexo(self):
        data = [1234, 1777]
        res = [4660, 6007]
        self.assertEqual(UFO(len(data), data, False), res)

if __name__ == '__main__':
    unittest.main()
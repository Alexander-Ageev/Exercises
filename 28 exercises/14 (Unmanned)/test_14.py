import unittest
from main import Unmanned

class main_tests(unittest.TestCase):
    def test_basic(self):
        L = 10
        N = 2
        track = [ [3, 5, 5], [5, 2, 2] ]
        res = 12
        self.assertEqual(Unmanned( L, len(track), track), res)
    def test_all_green(self):
        L = 10
        N = 1
        track = [ [1, 1, 1] ]
        res = 10
        self.assertEqual(Unmanned( L, len(track), track), res)
    def test_all_red(self):
        L = 10
        N = 3
        track = [ [2, 3, 3], [4, 2, 2], [6, 3, 3] ]
        res = 13
        self.assertEqual(Unmanned( L, len(track), track), res)
    def test_long_red(self):
        L = 10
        N = 2
        track = [ [0, 5, 1], [1, 5, 1] ]
        res = 20
        self.assertEqual(Unmanned( L, len(track), track), res)
    def test_lights_so_far(self):
        L = 10
        N = 2
        track = [ [11, 5, 5], [15, 2, 2] ]
        res = 10
        self.assertEqual(Unmanned( L, len(track), track), res)
    def test_inter_lights(self):
        L = 10
        N = 2
        track = [ [3, 5, 5], [15, 2, 2] ]
        res = 12
        self.assertEqual(Unmanned( L, len(track), track), res)


if __name__ == '__main__':
    unittest.main()
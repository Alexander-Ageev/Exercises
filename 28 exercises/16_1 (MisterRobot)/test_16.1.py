import unittest
import random
from main import MisterRobot

class main_tests(unittest.TestCase):
    def test_basic(self):
        data = [1,3,4,5,6,2,7]
        res = True
        self.assertEqual( MisterRobot(len(data), data), res )
    def test_true(self):
        data = [1,2,3,4]
        res = True
        self.assertEqual( MisterRobot(len(data), data), res )
    def test_reverse(self):
        data = [9,8,7,6,5,4,3,2,1]
        res = True
        self.assertEqual( MisterRobot(len(data), data), res )
    def test_False(self):
        data = [1,2,3,5,4]
        res = False
        self.assertEqual( MisterRobot(len(data), data), res )

if __name__ == '__main__':
    unittest.main()
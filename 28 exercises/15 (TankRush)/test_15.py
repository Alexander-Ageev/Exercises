import unittest
from main import TankRush

class main_tests(unittest.TestCase):
    def test_true(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 2
        W2 = 2
        S2 = '34 98'
        res = True
        self.assertEqual( TankRush(H1, W1, S1, H2, W2, S2), res )
    def test_false(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 2
        W2 = 2
        S2 = '35 97'
        res = False
        self.assertEqual( TankRush(H1, W1, S1, H2, W2, S2), res )
    def test_half(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 2
        W2 = 2
        S2 = '34 97'
        res = False
        self.assertEqual( TankRush(H1, W1, S1, H2, W2, S2), res )
    def test_enemy_around(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 3
        W2 = 4
        S2 = '1234 2345 0987'
        res = True
        self.assertEqual( TankRush(H1, W1, S1, H2, W2, S2), res )
    def test_saboteur(self):
        H1 = 3
        W1 = 4
        S1 = '1234 2345 0987'
        H2 = 1
        W2 = 1
        S2 = '7'
        res = True
        self.assertEqual( TankRush(H1, W1, S1, H2, W2, S2), res )
if __name__ == '__main__':
    unittest.main()
import unittest
import random
from main import ShopOLAP

class main_tests(unittest.TestCase):
    def test_basic(self):
        data = ['платье1 5',
                'сумка32 2',
                'платье1 1',
                'сумка23 2',
                'сумка128 4']
        res = ['платье1 6',
                'сумка128 4',
                'сумка23 2',
                'сумка32 2']
        self.assertEqual( ShopOLAP(len(data), data), res )
    
    def test_one_piece(self):
        data = ['платье1 5']
        res = ['платье1 5']
        self.assertEqual( ShopOLAP(len(data), data), res )

    def test_double(self):
        data = ['платье1 5',
                'платье2 5',
                'платье2 5']
        res = ['платье2 10',
                'платье1 5']
        self.assertEqual( ShopOLAP(len(data), data), res )

if __name__ == '__main__':
    unittest.main()
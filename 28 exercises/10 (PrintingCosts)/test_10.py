import unittest
from main import PrintingCosts


class main_tests(unittest.TestCase):
    def test_regression_all_symb(self):# точно истинный вариант
        s = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
        res = 1757
        self.assertEqual(PrintingCosts(s), res)
    def test_regression_incorrect_symb(self):# точно ложный вариант
        s = '®'
        res = 23
        self.assertEqual(PrintingCosts(s), res)
    def test_space(self):# точно ложный вариант
        s = '   '
        res = 0
        self.assertEqual(PrintingCosts(s), res)
    def test_many_incorrect_symb(self):# точно ложный вариант
        s = '®®®'
        res = 69
        self.assertEqual(PrintingCosts(s), res)
if __name__ == '__main__':
    unittest.main()
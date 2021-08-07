import unittest
from main import MatrixTurn

class main_tests(unittest.TestCase):
    def test_basic_64(self):
        data = ['123456',
                '234567',
                '345678',
                '456789']
        T = 1
        res =  ['212345',
                '343456',
                '456767',
                '567898']
        self.assertEqual(MatrixTurn(data, len(data), len(data[0]), T), res)

    def test_basic_64_3T(self):
        data = ['123456',
                '234567',
                '345678',
                '456789']
        T = 3
        res =  ['432123',
                '565434',
                '676545',
                '789876']
        self.assertEqual(MatrixTurn(data, len(data), len(data[0]), T), res)

    def test_basic_44(self):
        data = ['1234',
                '2345',
                '3456',
                '4567']
        T = 1
        res =  ['2123',
                '3434',
                '4545',
                '5676']
        self.assertEqual(MatrixTurn(data, len(data), len(data[0]), T), res)

    def test_basic_22(self):
        data = ['12',
                '34']
        T = 4
        res =  ['12',
                '34']
        self.assertEqual(MatrixTurn(data, len(data), len(data[0]), T), res)

    def test_basic_28(self):
        data = ['12345678',
                '87654321']
        T = 4
        res =  ['56781234',
                '43218765']
        self.assertEqual(MatrixTurn(data, len(data), len(data[0]), T), res)






if __name__ == '__main__':
    unittest.main()
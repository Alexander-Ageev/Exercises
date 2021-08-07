import unittest
from main import split_string, find_symbol, white_walkers

class main_tests(unittest.TestCase):
# split_string tests
    def test_split_string_basic(self):
        data = 'a1b2c3d'
        res =  [['a', 'b', 'c', 'd'], [1, 2, 3]]
        self.assertEqual(split_string(data), res)

    def test_split_string_empty_start(self):
        data = '1b2c3'
        res =  [['', 'b', 'c', ''], [1, 2, 3]]
        self.assertEqual(split_string(data), res)

    def test_split_string_no_numbers(self):
        data = 'abc'
        res =  [['abc'], []]
        self.assertEqual(split_string(data), res)

    def test_split_string_no_text(self):
        data = '1'
        res =  [['', ''], [1]]
        self.assertEqual(split_string(data), res)
# find_symbol tests
    def test_find_symbol_basic(self):
        data = 'abc'
        sym =  'b'
        res =  1
        self.assertEqual(find_symbol(data, sym), res)

    def test_find_symbol_no(self):
        data = 'ac'
        sym =  'b'
        res =  0
        self.assertEqual(find_symbol(data, sym), res)

    def test_find_symbol_many_symbol(self):
        data = 'abcbsbrbb'
        sym =  'b'
        res =  5
        self.assertEqual(find_symbol(data, sym), res)
# white_walkers tests
    def test_white_walkers_basic_1(self):
        data = 'axxb6===4xaf5===eee5'
        res =  True
        self.assertEqual(white_walkers(data), res)    

    def test_white_walkers_basic_2(self):
        data = '5==ooooooo=5=5'
        res =  False
        self.assertEqual(white_walkers(data), res) 

    def test_white_walkers_basic_3(self):
        data = 'abc=7==hdjs=3gg1=======5'
        res =  True
        self.assertEqual(white_walkers(data), res) 

    def test_white_walkers_basic_4(self):
        data = 'aaS=8'
        res =  False
        self.assertEqual(white_walkers(data), res) 

    def test_white_walkers_basic_5(self):
        data = '9===1===9===1===9'
        res =  True
        self.assertEqual(white_walkers(data), res) 

if __name__ == '__main__':
    unittest.main()
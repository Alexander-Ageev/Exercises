import unittest, random
from main import NativeDictionary

class main_tests(unittest.TestCase):
    def test_hash_fun_0(self):
        H = NativeDictionary(11)
        input_str = '!'
        data = H.hash_fun(input_str)
        res = 0
        self.assertEqual(data, res)
    
    def test_hash_fun_1(self):
        H = NativeDictionary(11)
        input_str = 'x'
        data = H.hash_fun(input_str)
        res = 10
        self.assertEqual(data, res)

    def test_put_new(self):
        H = NativeDictionary(11)
        H.put('x', 10)
        data = [H.slots[10], H.values[10]]
        res = ['x', 10]
        self.assertEqual(data, res)

    def test_put_replace(self):
        H = NativeDictionary(11)
        H.put('x', 10)
        H.put('x', 100)
        data = [H.slots[10], H.values[10]]
        res = ['x', 100]
        self.assertEqual(data, res)

    def test_get_key(self):
        H = NativeDictionary(11)
        H.put('x', 10)
        H.put('x', 100)
        data = H.get('x')
        res = 100
        self.assertEqual(data, res)

    def test_is_key_wrong_key(self):
        H = NativeDictionary(11)
        H.put('m', 10)
        data = H.is_key('x')
        res = False
        self.assertEqual(data, res)

    def test_get_none(self):
        H = NativeDictionary(11)
        H.put('x', 10)
        H.put('x', 100)
        data = H.get('z')
        res = None
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()
import unittest, random
from main import BloomFilter

class main_tests(unittest.TestCase):
    def test_true(self):
        b = BloomFilter(32)
        str1 = '1234567890'
        b.add(str1)
        data = b.is_value(str1)
        res =  True
        self.assertEqual(data, res)

    def test_false(self):
        b = BloomFilter(32)
        str1 = '1234567890'
        b.add(str1)
        data = b.is_value('0123456789')
        res =  False
        self.assertEqual(data, res)
    
    def test_list(self):
        b = BloomFilter(32)
        str_list = []
        str1 = '0123456789'
        str_list.append(str1)
        for i in range(1,10):
            str1 = str1[1:10] + str1[0]
            b.add(str1)
            str_list.append(str1)
        data = []
        for i in str_list:
            data.append(b.is_value(i))
        res =  [True] * 10
        self.assertEqual(data, res)
    
    def test_random(self):
        b = BloomFilter(32)
        str_list = []
        str1 = '0123456789'
        str_list.append(str1)
        for i in range(1,10):
            str1 = str1[1:10] + str1[0]
            b.add(str1)
            str_list.append(str1)
        for i in range(1):
            r = ''.join(random.sample('0123456789',10))
            data = b.is_value(r)
            res =  r in str_list
            self.assertEqual(data, res)
    
    def test_fantom(self):
        b = BloomFilter(32)
        str1 = '6791082435'
        b.add(str1)
        data = b.is_value('0123456789')
        res =  True
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()
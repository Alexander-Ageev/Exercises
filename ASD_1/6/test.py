import unittest
from main import Deque, palindrom_detector

class main_tests(unittest.TestCase):
    def test_addFront(self):
        deq = Deque()
        deq.addFront(1)
        deq.addFront(2)
        deq.addFront(3)       
        data = deq.get_data()
        res = [3, 2, 1]
        self.assertEqual(data, res)
    
    def test_addTail(self):
        deq = Deque()
        deq.addTail(1)
        deq.addTail(2)
        deq.addTail(3)       
        data = deq.get_data()
        res = [1, 2, 3]
        self.assertEqual(data, res)

    def test_addBooth(self):
        deq = Deque()
        deq.addFront(1)
        deq.addTail(2)
        data = deq.get_data()
        res = [1, 2]
        self.assertEqual(data, res)

    def test_removeFront(self):
        deq = Deque()
        deq.addFront(1)
        deq.addFront(2)
        deq.addFront(3)
        rem = []
        rem.append(deq.removeFront())
        rem.append(deq.removeFront())
        data = deq.get_data() + rem
        res = [1, 3, 2]
        self.assertEqual(data, res)

    def test_removeTail(self):
        deq = Deque()
        deq.addFront(1)
        deq.addFront(2)
        deq.addFront(3)
        rem = []
        rem.append(deq.removeTail())
        rem.append(deq.removeTail())
        data = deq.get_data() + rem
        res = [3, 1, 2]
        self.assertEqual(data, res)

    def test_size(self):
        deq = Deque()
        deq.addFront(1)
        deq.addFront(2)
        deq.addFront(3)
        data = deq.size()
        res = 3
        self.assertEqual(data, res)

    def test_pal_even_true(self):
        data = palindrom_detector('asdffdsa')
        res = True
        self.assertEqual(data, res)

    def test_pal_odd_true(self):
        data = palindrom_detector('asdfdsa')
        res = True
        self.assertEqual(data, res)

    def test_pal_char_true(self):
        data = palindrom_detector('a')
        res = True
        self.assertEqual(data, res)

    def test_pal_two_char_true(self):
        data = palindrom_detector('aa')
        res = True
        self.assertEqual(data, res)

    def test_pal_two_char_false(self):
        data = palindrom_detector('ab')
        res = False
        self.assertEqual(data, res)

    def test_pal_false(self):
        data = palindrom_detector('asdf')
        res = False
        self.assertEqual(data, res)

    def test_pal_false(self):
        data = palindrom_detector('asd')
        res = False
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()
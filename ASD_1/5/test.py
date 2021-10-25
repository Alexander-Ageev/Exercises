import unittest
from main import Queue, rotate
#from two_stacks import Queue 

class main_tests(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        data = q.get_data()
        res = [1, 2, 3]
        self.assertEqual( (data), res)
    
    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.dequeue()
        q.enqueue(3)
        data = q.get_data()
        res = [2, 3]
        self.assertEqual( (data), res)
    
    def test_dequeue_none(self):
        q = Queue()
        data = q.dequeue()
        res = None
        self.assertEqual( (data), res)
    
    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.dequeue()
        q.enqueue(3)
        data = q.size()
        res = 2
        self.assertEqual( (data), res)

    def test_rotate(self):
        q = Queue()
        for i in range (5):
            q.enqueue(i)
        data = rotate(q, 3)
        res = [3, 4, 0, 1, 2]
        self.assertEqual( (data), res)


if __name__ == '__main__':
    unittest.main()
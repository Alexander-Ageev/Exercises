import unittest
from main import Heap

class MainTest(unittest.TestCase):
    def test_add_array(self):
        heap = Heap()
        array = [1, 2, 3]
        heap.MakeHeap(array, 1)
        data = heap.GetHeap()
        res = [3, 1, 2]
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()
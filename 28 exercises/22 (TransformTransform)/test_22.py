import unittest
from main import TransformTransform

class main_tests(unittest.TestCase):
    def test_true(self):
        data = [2]
        res =  True
        self.assertEqual(TransformTransform(data, len(data)), res)
    
    def test_false(self):
        data = [1]
        res =  False
        self.assertEqual(TransformTransform(data, len(data)), res)


if __name__ == '__main__':
    unittest.main()
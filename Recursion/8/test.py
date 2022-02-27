import unittest
from main import get_filenames

class MainTest(unittest.TestCase):
    def test_simple(self):
        """Directory hierarchy"""
        data = 'G:/Хобби/Модели для принтера'
        res = 52
        self.assertEqual(get_filenames(data), res)

    def test_empty_dir(self):
        """Empty dir"""
        data = 'G:/Хобби/temp'
        res = 0
        self.assertEqual(get_filenames(data), res)

if __name__ == '__main__':
    unittest.main()

import unittest
from main import TreeOfLife

class main_tests(unittest.TestCase):
    def test_1(self):
        data = [".+..","..+.",".+.."]
        N = 12
        res = [".+..","..+.",".+.."]
        self.assertEqual(TreeOfLife(len(data), len(data[0]), N, data), res)

    def test_2(self):
        data = ['.......','...+...','....+..','.......','++.....','++.....']
        N = 24
        res = ['.......','...+...','....+..','.......','++.....','++.....']
        self.assertEqual(TreeOfLife(len(data), len(data[0]), N, data), res) 

if __name__ == '__main__':
    unittest.main()
import unittest
import random
from main import LineAnalysis

class main_tests(unittest.TestCase):
    def test_one_star(self):
        line = '*'
        res = True
        self.assertEqual( LineAnalysis(line), res )
    def test_two_star(self):
        line = '**'
        res = True
        self.assertEqual( LineAnalysis(line), res )
    def test_all_stars(self):
        line = '***'
        res = True
        self.assertEqual( LineAnalysis(line), res )
    def test_star_dot(self):
        line = '*.*'
        res = True
        self.assertEqual( LineAnalysis(line), res )
    def test_star_many_dot(self):
        line = '*.......*.......*'
        res = True
        self.assertEqual( LineAnalysis(line), res )
    def test_one_star_two_dot(self):
        line = '*..*..*..*..*..*..*'
        res = True
        self.assertEqual( LineAnalysis(line), res )
    def test_wrong_more_dot(self):
        line = '*..*...*..*..*..*..*'
        res = False
        self.assertEqual( LineAnalysis(line), res )
    def test_wrong_more_star(self):
        line = '*..*..*..*..*..**..*'
        res = False
        self.assertEqual( LineAnalysis(line), res )
    def test_wrong_star_and_dot(self):
        line = '*..*...*..*..*..**..*'
        res = False
        self.assertEqual( LineAnalysis(line), res )
    def test_miss_star(self):
        line = '**.*.**'
        res = False
        self.assertEqual( LineAnalysis(line), res )


# Данный тест может выдавать ложно-ошибочные строки (******.******, *.*.*.*.*).
    def test_random(self):
        for n in range(1000):
            count_star = random.randint(1, 3)
            count_dot = random.randint(1, 3)
            line = ''
            res = True
            for i in range(5):
                wrong_dot = random.randint(-count_dot, count_dot) * random.randint(0, 1)
                wrong_star = random.randint(-count_star , count_star) * random.randint(0, 1)
                line += '.' * (wrong_dot + count_dot)
                line += '*' * (wrong_star + count_star)
                if wrong_star != 0 or wrong_dot != 0:
                    res = False
            line = '*' * count_star + line
            self.assertEqual( LineAnalysis(line), res )

    def test_miss_end_star(self):
        line = '***..***..***..***..***..*'
        res = False
        self.assertEqual( LineAnalysis(line), res )




if __name__ == '__main__':
    unittest.main()
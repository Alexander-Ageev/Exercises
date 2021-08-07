import unittest
from main import MassVote
import random

class main_tests(unittest.TestCase):
    def test_win1(self):
        Votes = [60, 10, 10, 15, 5]
        res = 'majority winner 1'
        self.assertEqual(MassVote(len(Votes), Votes), res)
    def test_win2(self):
        Votes = [10, 15, 10]
        res = 'minority winner 2'
        self.assertEqual(MassVote(len(Votes), Votes), res)
    def test_no_winner(self):
        Votes = [111, 111, 110, 110]
        res = 'no winner'
        self.assertEqual(MassVote(len(Votes), Votes), res)
    def test_one_votes(self):
        Votes = [111]
        res = 'majority winner 1'
        self.assertEqual(MassVote(len(Votes), Votes), res)
    def test_accuracy(self):
        Votes = [99997, 100002, 100001, 50000, 75000, 75000]
        res = 'no winner'
        self.assertEqual(MassVote(len(Votes), Votes), res)
    def test_random_maj_winner(self):
        for i in range(100000):
            Votes = [random.randint(10, 100) for i in range(10)]
            index = random.randint(0, 9)
            Votes[index] = 1000
            res = 'majority winner ' + str(index+1)
            self.assertEqual(MassVote(len(Votes), Votes), res)
    def test_random_min_winner(self):
        for i in range(100000):
            Votes = [random.randint(10, 100) for i in range(10)]
            index = random.randint(0, 9)
            Votes[index] = 110
            res = 'minority winner ' + str(index+1)
            self.assertEqual(MassVote(len(Votes), Votes), res)


if __name__ == '__main__':
    unittest.main()
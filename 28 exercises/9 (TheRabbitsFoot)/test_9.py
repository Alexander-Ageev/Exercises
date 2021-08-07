import unittest
from main import TheRabbitsFoot

class main_tests(unittest.TestCase):
    def test_encode(self):
        s = 'отдай мою кроличью лапку'
        res = 'омоюу толл дюиа акчп йрьк'
        self.assertEqual(TheRabbitsFoot(s, True), res)

    def test_decode(self):
        s = 'омоюу толл дюиа акчп йрьк'
        res = 'отдаймоюкроличьюлапку'
        self.assertEqual(TheRabbitsFoot(s, False), res)


if __name__ == '__main__':
    unittest.main()
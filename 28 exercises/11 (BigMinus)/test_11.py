import unittest
import random
from main import BigMinus

class main_tests(unittest.TestCase):
    def test_simple(self):
        s1 = '123456789'
        s2 = '123'
        test = str( abs( int(s1) - int(s2) ) )
        self.assertEqual(BigMinus(s1, s2), test)
    def test_abs(self):
        s1 = '0'
        s2 = '1'
        test = str( abs( int(s1) - int(s2) ) )
        self.assertEqual(BigMinus(s1, s2), test)    
    def test_mode(self):
        s1 = '1000000'
        s2 = '9999'
        test = str( abs( int(s1) - int(s2) ) )
        self.assertEqual(BigMinus(s1, s2), test)    
    def test_reverse_simple(self):
        s1 = '123456789'
        s2 = '123'
        test = str( abs( int(s2) - int(s1) ) )
        self.assertEqual(BigMinus(s2, s1), test)
    def test_max_simple(self):
        s1 = '05048759779414119005038510062289068160'
        s2 = '5869766005497162628819483892411104020636238'
        test = str( abs( int(s1) - int(s2) ) )
        self.assertEqual(BigMinus(s2, s1), test)

  

    def test_random(self):
        for i in range(10000):
            num_of_s1 = random.randint(7, 20)
            num_of_s2 = random.randint(7, 20)
            s1 = ''
            s2 = ''
            for i in range(num_of_s1):
                s1 = str(random.randint(0, 9)) + s1
            for i in range(num_of_s2):
                s2 = str(random.randint(0, 9)) + s2
            s1 = s1.lstrip('0')
            s2 = s2.lstrip('0')
            test = str( abs( int(s1) - int(s2) ) )
            self.assertEqual(BigMinus(s1, s2), test)
# Тестирование нулевыми значениями
    def test_s1_null(self):
        s1 = '0'
        s2 = '123456789'
        test = str( abs( int(s1) - int(s2) ) )
        self.assertEqual(BigMinus(s1, s2), test)
    def test_s2_null(self):
        s2 = '0'
        s1 = '123456789'
        test = str( abs( int(s1) - int(s2) ) )
        self.assertEqual(BigMinus(s1, s2), test)
    def test_null_result(self):
        s1 = '123456789'
        test = str( abs( int(s1) - int(s1) ) )
        self.assertEqual(BigMinus(s1, s1), test)

# Тестирование максимальными значениями
    def test_max(self):
        num_of_s1 = random.randint(50, 500)
        num_of_s2 = random.randint(50, 500)
        s1 = ''
        s2 = ''
        for i in range(num_of_s1):
            s1 = str(random.randint(0, 9)) + s1
        for i in range(num_of_s2):
            s2 = str(random.randint(0, 9)) + s2
        test = str( abs( int(s1) - int(s2) ) )
        self.assertEqual(BigMinus(s1, s2), test)

if __name__ == '__main__':
    unittest.main()
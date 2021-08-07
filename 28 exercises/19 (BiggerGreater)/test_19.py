import unittest
import random
from main import BiggerGreater

class main_tests(unittest.TestCase):
    def test_smal_word(self):
        data = 'ая'
        res = 'яа'
        self.assertEqual( BiggerGreater('ая'), res )
    
    def test_simple_word(self):
        data = 'вибк'
        res = 'викб'
        self.assertEqual( BiggerGreater('вибк'), res )

    def test_reverse_word(self):
        data = 'вкиб'
        res = 'ибвк'
        self.assertEqual( BiggerGreater('вкиб'), res )

    def test_double_char_word(self):
        data = 'assa'
        res = 'saas'
        self.assertEqual( BiggerGreater('assa'), res )

    def test_one_char_word(self):
        data = 'ssss'
        res = ''
        self.assertEqual( BiggerGreater('ssss'), res )

    def test_biggest_word(self):
        data = 'dcba'
        res = ''
        self.assertEqual( BiggerGreater('dcba'), res )     

    def test_overload_word(self):
        data = 'fgedcba'
        res = 'gabcdef'
        self.assertEqual( BiggerGreater('fgedcba'), res )     

    def test_two_char_word(self):
        data = 'abaaaaa'
        res =  'baaaaaa'
        self.assertEqual( BiggerGreater('abaaaaa'), res )     

    def test_za_word(self):
        data = 'za'
        res =  ''
        self.assertEqual( BiggerGreater('za'), res )     

    def test_yo(self):
        data = 'ёж'
        res =  'жё'
        self.assertEqual( BiggerGreater('ёж'), res )   


if __name__ == '__main__':
    unittest.main()



import unittest
import random
from main import BastShoe

class main_tests(unittest.TestCase):
    def test_basic(self):
        data = test = ['1 Привет', # add text test
                        '1 , Мир!', # add text test
                        '1 ++', # add text test
                        '2 2', # delete text test
                        '4', # undo test
                        '4',
                        '1 *', #undo reset test
                        '4',
                        '4',
                        '4', # more undo test
                        '3 6', # index test
                        '2 100', # clear test
                        '1 Привет',
                        '1 , Мир!',
                        '1 ++',
                        '4',
                        '4',
                        '5',
                        '4',
                        '5',
                        '5',
                        '5',
                        '5', # more redo test
                        '4',
                        '4',
                        '2 2', # undo reset test
                        '4',
                        '5',
                        '5',
                        '5'] # redo overindex test
        res = ['Привет',
                'Привет, Мир!',
                'Привет, Мир!++',
                'Привет, Мир!',
                'Привет, Мир!++',
                'Привет, Мир!',
                'Привет, Мир!*',
                'Привет, Мир!',
                'Привет, Мир!',
                'Привет, Мир!',
                ',',
                '',
               'Привет',
               'Привет, Мир!',
               'Привет, Мир!++',
               'Привет, Мир!',
               'Привет',
               'Привет, Мир!',
               'Привет',
               'Привет, Мир!',
               'Привет, Мир!++',
               'Привет, Мир!++',
               'Привет, Мир!++',
               'Привет, Мир!',
               'Привет',
               'Прив',
               'Привет',
               'Прив',
               'Прив',
               'Прив']
        for i in range(len(data)):
            self.assertEqual( BastShoe(data[i]), res[i] )
    def test_index_out_of_range(self):
        data = ['2 100', '1 qwe', '3 100']
        res = ['', 'qwe', '']
        for i in range(len(data)):
            self.assertEqual( BastShoe(data[i]), res[i] )      

if __name__ == '__main__':
    unittest.main()

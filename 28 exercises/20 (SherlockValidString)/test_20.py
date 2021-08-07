import unittest
import random
from main import SherlockValidString

class main_tests(unittest.TestCase):
    def test_xyz_true(self):
        data = 'xyz'
        res = True
        self.assertEqual(SherlockValidString(data), res)
    def test_xyzaa_true(self):
        data = 'xyzaa'
        res = True
        self.assertEqual(SherlockValidString(data), res)
    def test_xxyyz_true(self):
        data = 'xxyyz'
        res = True
        self.assertEqual(SherlockValidString(data), res)
    def test_xxxyyyzzza_true(self):
        data = 'xxxyyyzzza'
        res = True
        self.assertEqual(SherlockValidString(data), res)
    def test_xxxxxyyyyyy_true (self):
        data = 'xxxxxyyyyyy'
        res = True
        self.assertEqual(SherlockValidString(data), res)
    def test_xyy_true (self):
        data = 'xyy'
        res = True
        self.assertEqual(SherlockValidString(data), res)
    def test_xyzzz_false(self):
        data = 'xyzzz'
        res = False
        self.assertEqual(SherlockValidString(data), res)
    def test_xxyyza_false(self):
        data = 'xxyyza'
        res = False
        self.assertEqual(SherlockValidString(data), res)
    def test_xxyyzabc_false(self):
        data = 'xxyyzabc'
        res = False
        self.assertEqual(SherlockValidString(data), res)
    def test_xyyzzz_false(self):
        data = 'xyyzzz'
        res = False
        self.assertEqual(SherlockValidString(data), res)

    def test_random(self):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        for i in range(100):
            base = random.randint(1, 4)
            res_string = ''
            error_count = 0
            error_flag = 0
            for i in chars:
                error = random.randint(-1, 2)
                if -(base) != error:
                    if error == 1 or error == -1:
                        error_count += 1
                    if error == 2:
                        error_flag += 1
                    res_string += i * (base + error)
            
            data = res_string
            if error_count > 1 or error_flag > 0:
                res = False
            else:
                res = True
            self.assertEqual(SherlockValidString(data), res)




if __name__ == '__main__':
    unittest.main()

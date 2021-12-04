import unittest, random, cProfile
from main import PowerSet

def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper



class main_tests(unittest.TestCase):
    def test_put_new(self):
        ps = PowerSet()
        input_str = '!'
        ps.put(input_str)
        data = ps.list_value()
        res = [input_str]
        self.assertEqual(data, res)

    def test_put_old(self):
        ps = PowerSet()
        input_str = '!'
        ps.put(input_str)
        ps.put(input_str)
        data = ps.list_value()
        res = [input_str]
        self.assertEqual(data, res)

    def test_put_remove(self):
        ps = PowerSet()
        ps.put('123')
        ps.put('546')
        ps.remove('546')
        data = ps.list_value()
        res = ['123']
        self.assertEqual(data, res)

    def test_put_remove_none(self):
        ps = PowerSet()
        ps.put('0')
        ps.put(':')
        ps.put('D')
        ps.remove('1')
        data = sorted(ps.list_value())
        res = sorted(['0', ':', 'D'])
        self.assertEqual(data, res)

    def test_put_remove_step(self):
        ps = PowerSet()
        ps.put('0')
        ps.put(':')
        ps.put('D')
        ps.remove(':')
        data = sorted(ps.list_value())
        res = sorted(['0', 'D'])
        self.assertEqual(data, res)

    def test_intersection_true(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set1.put('0')
        set1.put(':')
        set1.put('D')
        set2.put('1')
        set2.put(':')
        set2.put('D')
        data = sorted(set1.intersection(set2).list_value())
        res = sorted([':', 'D'])
        self.assertEqual(data, res)
    
    def test_intersection_void(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set1.put('0')
        set1.put(':')
        set1.put('D')
        set2.put('1')
        set2.put('2')
        set2.put('3')
        data = sorted(set1.intersection(set2).list_value())
        res = sorted([])
        self.assertEqual(data, res)

    @profile
    def test_intersection_random(self):
        set1 = PowerSet()
        set1_list = []
        set2 = PowerSet()
        set2_list = []
        for i in range(20000):
            a = str(random.randint(0,100000))
            b = str(random.randint(0,100000))
            set1.put(a)
            set1_list.append(a)
            set2.put(b)
            set2_list.append(b)
        a = set(set1_list)
        b = set(set2_list)
        data = sorted(set1.intersection(set2).list_value())
        res = sorted(list(a & b))
        self.assertEqual(data, res)

    def test_union_random(self):
        set1 = PowerSet()
        set1_list = []
        set2 = PowerSet()
        set2_list = []
        for i in range(100):
            a = str(random.randint(0,9))
            b = str(random.randint(0,9))
            set1.put(a)
            set1_list.append(a)
            set2.put(b)
            set2_list.append(b)
        a = set(set1_list)
        b = set(set2_list)
        data = sorted(set1.intersection(set2).list_value())
        res = sorted(list(a | b))
        self.assertEqual(data, res)



if __name__ == '__main__':
    unittest.main()
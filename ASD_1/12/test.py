import unittest, random
from main import NativeCache

class main_tests(unittest.TestCase):
    def test_true(self):
        Johny = NativeCache(100)
        Johny.put('123', 10)
        data = Johny.get('123')
        res =  10
        self.assertEqual(data, res)

    def test_collision(self):
        Johny = NativeCache(100)
        for i in range(100):
            Johny.put(i, i)
        get_list = [0 for i in range(100)]
        for i in range(1000):
            p = random.randint(0, 99)
            Johny.get(p)
            get_list[p]+=1
        Johny.put(101, 101)       
        index = get_list.index(min(get_list))
        get_list[index] = 101
        data = Johny.get(101)
        res = 101
        self.assertEqual(data, res)
if __name__ == '__main__':
    unittest.main()
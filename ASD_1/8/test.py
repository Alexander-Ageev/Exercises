import unittest, random
from main import HashTable

class main_tests(unittest.TestCase):
    def test_hash_fun_0(self):
        H = HashTable(11, 2)
        input_str = '!'
        data = H.hash_fun(input_str)
        res = 0
        self.assertEqual(data, res)
    
    def test_hash_fun_1(self):
        H = HashTable(11, 2)
        input_str = 'x'
        data = H.hash_fun(input_str)
        res = 10
        self.assertEqual(data, res)

    def test_seek_slot_free_slot(self):  
        H = HashTable(11, 3)
        input_str = 'x'
        data = H.seek_slot(input_str)
        res = 10
        self.assertEqual(data, res)
        
    def test_seek_slot_busy_slot(self):  
        H = HashTable(11, 3)
        input_str = 'x'
        H.slots[10] = '123'
        data = H.seek_slot(input_str)
        res = 2
        self.assertEqual(data, res)
    
    def test_seek_slot_full(self):  
        H = HashTable(11, 3)
        for i in range(11):
            H.slots[i] = '1'
        input_str = 'x'
        data = H.seek_slot(input_str)
        res = None
        self.assertEqual(data, res)

    def test_seek_slot_full_cycle(self):  
        H = HashTable(9, 3)
        for i in range(9):
            H.slots[i] = '1'
        input_str = 'x'
        data = H.seek_slot(input_str)
        res = None
        self.assertEqual(data, res)
    
    def test_put_to_full(self):  
        H = HashTable(11, 1)
        ind_list = []
        
        for i in range(11):
            ind_list.append(H.put(chr(44 + i)))
        data = H.slots + ind_list
        res = [',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6'] + list(range(11))
        self.assertEqual(data, res)

    def test_put_to_full_with_step(self):  
        H = HashTable(11, 1)
        ind_list = []
        for i in range(11):
            ind_list.append(H.put(chr(44)))
        data = H.slots + ind_list
        res = [',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ','] + list(range(11))
        self.assertEqual(data, res)

    def test_find_simple(self):
        H = HashTable(11,1)
        data = H.put('x')
        res = H.find('x')
        self.assertEqual(data, res)

    def test_find_all(self):  
        ref_list = ['!', ',', '7', 'B', 'M', 'X', 'c', 'n', 'y', '\x84', '\x8f', '5']
        H = HashTable(11, 1)
        ind_list = []
        res = []
        for i in range(11):
            H.put(chr(33 + i * 11))
            #['!', ',', '7', 'B', 'M', 'X', 'c', 'n', 'y', '\x84', '\x8f']
        for i in range(12):
            rnd_index = random.randint(0, 11)
            ind_list.append(H.find(ref_list[rnd_index]))
            if rnd_index == 11:
                res.append(None)
            else:
                res.append(rnd_index)
        ind_list.append(H.find(''))
        res.append(None)        
        data = ind_list
        self.assertEqual(data, res)
    
    def test_random(self):
        ref_char = []
        for i in range(32, 127):
            ref_char.append(chr(i))
        for i in range(1000):
            string_count = random.randint(0, 19)
            H = HashTable(19, 3)
            put_char_list = []
            find_char_list = []
            char_list = random.sample(ref_char, string_count)   
            for i in char_list:
                put_char_list.append(H.put(i))
            for i in char_list:
                find_char_list.append(H.find(i))
            data = put_char_list
            res = find_char_list
            self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()
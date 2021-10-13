import unittest
import random
from main import DynArray

class main_tests(unittest.TestCase):
    def test_insert_in_range_first(self):
        a = DynArray()
        for i in range(10):
            a.append(i)
        a.insert(0, 0)
        data = [a.capacity, a.__len__(), a.__getitem__(0)]
        res =  [16, 11, 0]
        self.assertEqual( data, res)

    def test_insert_in_range_middle(self):
        a = DynArray()
        for i in range(10):
            a.append(i)
        a.insert(5, 999)
        data = [a.capacity, a.__len__(), a.__getitem__(5), a.__getitem__(6)]
        res =  [16, 11, 999, 5]
        self.assertEqual( data, res)

    def test_insert_in_range_last_1(self):
        a = DynArray()
        for i in range(10):
            a.append(i)
        a.insert(10, 999)
        data = [a.capacity, a.__len__(), a.__getitem__(10)]
        res =  [16, 11, 999]
        self.assertEqual( data, res)

    def test_insert_in_range_last(self):
        a = DynArray()
        for i in range(15):
            a.append(i)
        a.insert(15, 999)
        data = [a.capacity, a.__len__(), a.__getitem__(15)]
        res =  [16, 16, 999]
        self.assertEqual( data, res)

    def test_insert_out_of_range(self):
        a = DynArray()
        for i in range(10):
            a.append(i)
        self.assertRaises(IndexError, a.insert, 11, 0)

    def test_insert_with_extension(self):
        a = DynArray()
        for i in range(16):
            a.append(i)
        a.insert(16, 999)
        data = [a.capacity, a.__len__(), a.__getitem__(16)]
        res =  [32, 17, 999]
        self.assertEqual( data, res)

    def test_insert_with_extension_1(self):
        a = DynArray()
        for i in range(16):
            a.append(i)
        a.insert(1, 999)
        data = [a.capacity, a.__len__(), a.__getitem__(1)]
        res =  [32, 17, 999]
        self.assertEqual( data, res)

    def test_delete_first(self):
        a = DynArray()
        for i in range(10):
            a.append(i)
        a.delete(0)
        data = [a.capacity, a.__len__(), a.__getitem__(0)]
        res =  [16, 9, 1]
        self.assertEqual( data, res)

    def test_delete_one(self):
        a = DynArray()
        for i in range(1):
            a.append(i)
        a.delete(0)
        data = [a.capacity, a.__len__()]
        res =  [16, 0]
        self.assertEqual( data, res)

    def test_delete_middle(self):
        a = DynArray()
        for i in range(10):
            a.append(i)
        a.delete(5)
        data = [a.capacity, a.__len__(), a.__getitem__(5)]
        res =  [16, 9, 6]
        self.assertEqual( data, res)

    def test_delete_last(self):
        a = DynArray()
        for i in range(16):
            a.append(i)
        a.delete(0)
        data = [a.capacity, a.__len__()]
        res =  [16, 15]
        self.assertEqual( data, res)

    def test_delete_with_resize(self):
        a = DynArray()
        for i in range(17):
            a.append(i)
        a.delete(16)
        a.delete(3)
        data = [a.capacity, a.__len__(), a.__getitem__(14)]
        res =  [21, 15, 15]
        self.assertEqual( data, res)


    def test_delete_with_resize_1(self):
        a = DynArray()
        for i in range(17):
            a.append(i)
        a.delete(16)
        a.delete(15)
        data = [a.capacity, a.__len__(), a.__getitem__(14)]
        res =  [21, 15, 14]
        self.assertEqual( data, res)

    def test_delete_error(self):
        a = DynArray()
        for i in range(16):
            a.append(i)
        self.assertRaises(IndexError, a.delete, 20)

    def test_radom(self):
        for i in range(1000):
            count_element = random.randint(0, 16)
            a = DynArray()
            a_list = []
            for i in range(count_element):
                a.append(i)
            insert_index = -1
            while not (-1 < insert_index < count_element +1):
                insert_index = random.randint(0, 16)
            a.insert(insert_index, 999)
            #print(f'array size: {count_element}, insert index: {insert_index}')
            #for i in range(count_element + 1):
            #    a_list.append(a.__getitem__(i))
            #print(a_list)
            data = [a.__len__(), a.__getitem__(insert_index)]
            res = [count_element+1, 999]
            self.assertEqual(data, res)

if __name__ == '__main__':  
    unittest.main()
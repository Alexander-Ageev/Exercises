"""Модуль содержит тесты для реализации класса Heap"""
import unittest
import random as rnd
from main import Heap

class MainTest(unittest.TestCase):
    def test_make_simple_heap(self):
        """Проверка на создание простой пирамиды"""
        heap = Heap()
        array = [1, 2, 3]
        heap.MakeHeap(array, 1)
        data = heap.GetHeap()
        res = [3, 1, 2]
        self.assertEqual(data, res)

    def test_make_oversize_heap(self):
        """Проверка на создание пирамиды с излишними входными данными"""
        heap = Heap()
        array = [1, 2, 3, 5, 7, 9]
        heap.MakeHeap(array, 1)
        data = heap.GetHeap()
        res = [3, 1, 2]
        self.assertEqual(data, res)

    def test_make_lowsize_heap(self):
        """Проверка на создание пирамиды со свободными ячейками"""
        heap = Heap()
        array = [1, 2, 3]
        heap.MakeHeap(array, 4)
        data = heap.GetHeap()
        res = [3, 1, 2]
        self.assertEqual(data, res)

    def test_make_empty_heap(self):
        """Проверка на создание пустой пирамиды"""
        heap = Heap()
        array = []
        heap.MakeHeap(array, 4)
        data = heap.GetHeap()
        res = []
        self.assertEqual(data, res)

    def test_add_duplicate_element(self):
        """Проверка на добавление существующего элемента"""
        heap = Heap()
        array = [1, 2, 3]
        heap.MakeHeap(array, 2)
        heap.Add(3)
        data = heap.GetHeap()
        res = [3, 3, 2, 1]
        self.assertEqual(data, res)

    def test_add_in_full_heap(self):
        """Проверка на создание простой пирамиды"""
        heap = Heap()
        array = [1, 2, 3]
        heap.MakeHeap(array, 1)
        add_ok = heap.Add(5)
        data = (add_ok, heap.GetHeap())
        res = (False, [3, 1, 2])
        self.assertEqual(data, res)

    def test_get_max(self):
        """Проверка на удаление корня"""
        heap = Heap()
        array = [1, 2, 3]
        heap.MakeHeap(array, 1)
        data = (heap.GetMax(), heap.GetHeap())
        res = (3, [2, 1])
        self.assertEqual(data, res)

    def test_get_all(self):
        """Проверка на удаление всех элементов"""
        heap = Heap()
        array = [1, 4, 3, 5, 2]
        heap.MakeHeap(array, 3)
        max_array = []
        for i in range(len(array)+1):
            max_array.append(heap.GetMax())
        data = (max_array, heap.GetHeap())
        res = ([5, 4, 3, 2, 1, -1], [])
        self.assertEqual(data, res)

    def test_random_heap_get_all(self):
        """Проверка добавления/удаления элементов на случайных значениях"""
        for i in range(1000):
            el_count = rnd.randint(0, 31)
            array = [rnd.randint(0, 100) for i in range(el_count)]
            heap = Heap()
            heap.MakeHeap(array, 4)
            data = []
            for element in array:
                data.append(heap.GetMax())
            array.sort(reverse= True)
            res = array
            self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()

"""Тесты для модуля, реализующего бинарное дерево поиска через массив"""
import unittest
from main import aBST

ROOT = 50
TEST_NODES = [25, 75, 37, 62, 84, 31, 43, 55, 92]

class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        """Создание тестового дерева"""
        self.tree = aBST(3)
        self.tree.AddKey(ROOT)
        for i in TEST_NODES:
            self.tree.AddKey(i)

    def test_tree_setup(self):
        """Проверка корректности создания тестового дерева"""
        res = (self.tree.tree_size, self.tree.Tree)
        data = (15, [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])
        self.assertEqual(res, data)

    def test_no_empty_slot(self):
        """Проверка на невозможность добавить новый ключ"""
        res = self.tree.FindKeyIndex(98)
        data = None
        self.assertEqual(res, data)

    def test_find_empty_slot_key(self):
        """Проверка на корректность поиска свободного слота"""
        res = self.tree.FindKeyIndex(22)
        data = -3
        self.assertEqual(data, res)

    def test_zero_index_key_equal(self):
        """Проверка на корректность работы метода FindKeyIndex. Все дерево занято, ключ найден"""
        tree = aBST(0)
        tree.AddKey(ROOT)
        res = tree.FindKeyIndex(50)
        data = 0
        self.assertEqual(data, res)

    def test_no_find_key_in_zero_depth(self):
        """Проверка на корректность работы метода FindKeyIndex. Все дерево занято, ключ не найден"""
        tree = aBST(0)
        tree.AddKey(ROOT)
        res = tree.FindKeyIndex(51)
        data = None
        self.assertEqual(data, res)

    def test_no_add_key_in_zero_depth(self):
        """Проверка на корректность работы метода AddKeyIndex. Все дерево занято, ключ не найден"""
        tree = aBST(0)
        tree.AddKey(ROOT)
        res = tree.AddKey(51)
        data = -1
        self.assertEqual(data, res)

    def test_add_exist_key(self):
        """Проверка на добавление существующего ключа"""
        res = self.tree.AddKey(50)
        data = 0
        print(self.tree.Tree)
        self.assertAlmostEqual(res, data)

    def test_full_tree(self):
        """Заплняем дерево, проверяем результат"""
        new_nodes = [22, 6, 76, 63, 59, 23]
        new_indexes = []
        for i in new_nodes:
            new_indexes.append(self.tree.AddKey(i))
        res = (self.tree.tree_size, self.tree.Tree, new_indexes)
        data = (15,
                [50, 25, 75, 22, 37, 62, 84, 6, 23, 31, 43, 55, 63, 76, 92],
                [3, 7, 13, 12, -1, 8])
        self.assertEqual(res, data)

if __name__ == "__main__":
    unittest.main()

"""
Модуль содержит реализацию бинарного дерева поиска через массив ключей.
Данная реализация расчитана только на добавление новых узлов (удаление узлов и ветвей невозможно)
"""

class aBST:
    def __init__(self, depth):
        """
        Инициализация объекта.
        depth - глубина бинарного дерева
        self.Tree - массив ключей дерева
        """
        tree_size = 0
        for i in range(depth):
            tree_size += 2 ** i
        self.tree_size = tree_size
        self.Tree = [None] * tree_size # массив ключей

    def FindKeyIndex(self, key):
        """Инициализация _FindKey_"""
        index = self._FindKey_(0, key)
        return index

    def AddKey(self, key):
        """
        Возвращает индекс добавленного ключа.
        Если нет свободного слота для нового ключа, возвращает -1
        """
        index = self._FindKey_(0, key)
        if index is None:
            index = -1
        elif index == 0 and self.Tree[index] is None:
            self.Tree[index] = key
        elif index == 0 and self.Tree[index] is not None:
            index = -1
        elif index < 0:
            index = abs(index)
            self.Tree[index] = key
        return index

    def _FindKey_(self, current_index, key):
        """
        Возвращает индекс узла в массиве, если ключ найден.
        Если ключ не найден, возвращает индекс подходящей свободной
        ячейки в массиве.
        Если свободной ячейки нет, возвращает None
        """
        if current_index >= self.tree_size:
            index = None
        elif self.Tree[current_index] is None:
            index = -1 * current_index
        elif self.Tree[current_index] == key:
            index = current_index
        elif key < self.Tree[current_index]:
            next_index = current_index * 2 + 1
            index = self._FindKey_(next_index, key)
        elif key > self.Tree[current_index]:
            next_index = current_index * 2 + 2
            index = self._FindKey_(next_index, key)
        return index

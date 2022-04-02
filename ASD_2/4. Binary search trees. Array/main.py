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
            tree_size += 2 ** depth
        self.tree_size = tree_size
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        """Возвращает индекс ключа, если ключ не найден - возвращает None."""
        search_result = self._FindKey_(0, key)
        if search_result[1] is True:
            index = search_result[0]
        else:
            index = None
        return index
	
    def AddKey(self, key):
        search_result = self._FindKey_(0, key)
        index = search_result[0]
        empty_node = not search_result[1]
        if empty_node is True:
            self.Tree[index] = key
        else:
            pass
            #TODO: добавить метод resize array
            #TODO: добавить ключ по новому адресу
        return -1; 
        # индекс добавленного/существующего ключа или -1 если не удалось

    def _FindKey_(self, current_index, key):
        if current_index >= self.tree_size - 1:
            current_index = (current_index-1) // 2
            return (current_index, False)
        if self.Tree[current_index] == key:
            return (current_index, True)
        elif key < self.Tree[current_index]:
            next_index = current_index * 2 + 1
            return self._FindKey_(next_index, key)
        elif key > self.Tree[current_index]:
            next_index = current_index * 2 + 2
            return self._FindKey_(next_index, key)
"""
Модуль описывает реализацию типа данных Пирамида через массив.
"""

class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
        self.MaxSize = 0
	
    def MakeHeap(self, a, depth):
        """
        Создает пирамиду из массива a.
        Максимальный размер массива определяется величиной depth.
        """
        self.MaxSize = 2 ** (depth+1) - 1
        if len(a) > self.MaxSize:
            a = a[0: self.MaxSize]
        for element in a:
            self.Add(element)   

    def GetMax(self):
        """
        Возвращает значение корня и перестраивает пирамиду.
        Возвращает -1, если пирамида пуста.
        """
        if len(self.HeapArray) == 0:
            return -1
        elif len(self.HeapArray) == 1:    
            root = self.HeapArray.pop(0)
        else:
            self.HeapArray[0], self.HeapArray[-1] = self.HeapArray[-1], self.HeapArray[0]
            root = self.HeapArray.pop(-1)
            self.MoveDown(self.HeapArray[0], 0)
        
        print('root:', root)

        return root

    def Add(self, key):
        """
        Добавляет элемент в пирамиду, перестраивая ее.
        Возвращает True при успешном добавлении элемента.
        Возвращает False, если пирамида заполнена.
        """
        if len(self.HeapArray) >= self.MaxSize:
            return False
        self.HeapArray.append(key)
        self.MoveUp(key, len(self.HeapArray)-1)
        return True

    def GetHeap(self):
        """Возвращает массив ключей пирамиды"""
        return self.HeapArray

    def MoveUp(self, key, index):
        """
        Перестраивает пирамиду просеиванием снизу вверх:
        если ключ-потомок больше ключа-родителя - меняет ключи местами
        """
        parent_index = (index - 1) // 2
        if key > self.HeapArray[parent_index] and index != 0:
            self.HeapArray[index], self.HeapArray[parent_index] = self.HeapArray[parent_index], key
            self.MoveUp(key, parent_index)

    def MoveDown(self, key, index):
        """
        Перестраивает пирамиду просеивая сверху вниз:
        если родитель меньше максимального из потомков -> родитель и потомок меняются местами.
        Операция повторяется, пока родитель не будет больше обоих своих потомков.
        """
        
        print('array:', self.HeapArray)
        
        left_child_index = 2 * index + 1
        childs = self.HeapArray[left_child_index: left_child_index + 2]
        max_child = max(childs)
        max_index = left_child_index + childs.index(max_child)

        print("max_index:", max_index)

        if max_index < len(self.HeapArray) and key < max_child:
            self.HeapArray[index], self.HeapArray[max_index] = self.HeapArray[max_index], self.HeapArray[index]
            self.MoveDown(key, max_index)

"""
Модуль описывает реализацию типа данных Пирамида через массив.
"""
class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
        self.max_size = 0
		
    def MakeHeap(self, a, depth):
        """
        Создает пирамиду из массива a.
        Максимальный размер массива определяется величиной depth.
        """
        self.max_size = 2 ** (depth+1) - 1
        if len(a) > self.max_size:
            a = a[0: self.max_size]
        for element in a:
            print('el:', element)
            self.Add(element)   

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        return -1 # если куча пуста

    def Add(self, key):
        """
        Добавляет элемент в пирамиду, перестраивая ее.
        Возвращает True при успешном добавлении элемента.
        Возвращает False, если пирамида заполнена.
        """
        if len(self.HeapArray) >= self.max_size:
            return False
        self.HeapArray.append(key)
        self.MoveUp(key, len(self.HeapArray)-1)
        return True
    
    def GetHeap(self):
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


    def MoveDown(self):
        pass
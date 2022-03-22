"""Модуль содержит реализацию типа данных БИНАРНОЕ ДЕРЕВО ПОИСКА"""

class BSTNode:
    """Класс описывает узел бинарного дерева поиска"""
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        """Создает объект с информацией о результатах поиска"""
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком
    
    def FindNode(self, current_node: BSTNode, parent_node: BSTNode, key):
        """Поиск узла по значению, либо родительского узла, куда необходимо значение добавить"""
        if current_node is None:
            self.Node = parent_node
            return self
        if current_node.NodeKey > key:
            self.ToLeft = True
            return self.FindNode(current_node.LeftChild, current_node, key)
        if current_node.NodeKey < key:
            self.ToLeft = False
            return self.FindNode(current_node.RightChild, current_node, key)
        if current_node.NodeKey == key:
            self.Node = current_node
            self.NodeHasKey = True
        return self

class BST:
    """Класс описывает структуру бинарного дереа поиска"""
    def __init__(self, node: BSTNode):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        """Возвращает ссылку на узел и сопутстующую информацтю поиска"""
        res = BSTFind()
        return res.FindNode(self.Root, self.Root.Parent, key)

    def AddKeyValue(self, key, val):
        res = self.FindNodeByKey(key) # добавляем ключ-значение в дерево
        if res.NodeHasKey == True:
            return False # если ключ уже есть
        if res.Node is None:
            self.Root = BSTNode(key, val, None)        
        if res.ToLeft == True:
            res.Node.LeftChild = BSTNode(key, val, res.Node)
        if res.ToLeft == False:
            res.Node.RightChild = BSTNode(key, val, res.Node)
        return True
  
    def FinMinMax(self, FromNode: BSTNode, FindMax: bool):
        """
        Возвращает ссылку на узел с максимальным/минимальным значением ключа
        FindMax = True - поиск максимума
        FindMax = False - поиск минимума
        """
        if FindMax == True: # Поиск максимума
            if FromNode.RightChild is not None:
                return self.FinMinMax(FromNode.RightChild, FindMax)
            return FromNode
        if FromNode.LeftChild is not None: # Поиск минимума
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        return FromNode
	
    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self):
        return 0 # количество узлов в дереве
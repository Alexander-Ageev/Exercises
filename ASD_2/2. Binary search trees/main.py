"""Модуль содержит реализацию типа данных БИНАРНОЕ ДЕРЕВО ПОИСКА"""

from platform import node


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
        """
        Создает объект с информацией о результатах поиска
        self.Node = None - если в дереве нет узлов
        self.NodeHasKey = False - если узел не найден
        self.ToLeft = True - если родительскому узлу надо 
        добавить новый узел левым потомком    
        """
        self.Node = None # None если в дереве вообще нету узлов
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
	
    def __IsLeaf__(self, node: BSTNode):
        """Возвращает True, если узел является листом"""
        no_child = node.LeftChild is None and node.RightChild is None
        return True if no_child else False

    def DeleteNodeByKey1(self, key):
        node_info = self.FindNodeByKey(key)# удаляем узел по ключу
        node = node_info.Node
        if node_info.NodeHasKey == False:
            return False
        if node is self.Root:
            return False
        #Случай, когда узел имеет два дочерних узла
        if node.LeftChild is not None and node.RightChild is not None:
            replace_node = self.FinMinMax(node.RightChild, False)
            if self.__IsLeaf__(replace_node):
                replace_node.Parent.LeftChild = None
            else:
                replace_node.Parent.LeftChild = replace_node.RightChild
                replace_node.RightChild.Parent = replace_node.Parent
            if node.NodeValue > node.Parent.NodeValue:
                node.Parent.RightChild = node.LeftChild
            else:
                node.Parent.LeftChild = node.LeftChild
            replace_node.Parent = node.Parent
            #node.Parent = None
            replace_node.LeftChild = node.LeftChild
            #node.LeftChild = None
            replace_node.RightChild = node.RightChild
            #node.RightChild = None
        #Если удаляемый узел имеет дочерний узел слева
        elif node.LeftChild is not None:
            if node.LeftChild.NodeValue > node.Parent.NodeValue:
                node.Parent.RightChild = node.LeftChild
            else:
                node.Parent.LeftChild = node.LeftChild
            node.LeftChild.Parent = node.Parent
        #Если удаляемый узел имеет дочерний узел справа
        elif node.RightChild is not None:
            if node.RightChild.NodeValue > node.Parent.NodeValue:
                node.Parent.RightChild = node.RightChild
            else:
                node.Parent.LeftChild = node.RightChild
            node.RightChild.Parent = node.Parent
        #Если удаляемый узел является листом
        elif self.__IsLeaf__(node):
            if node.NodeValue > node.Parent.NodeValue:
                node.Parent.RightChild = None
            else:
                node.Parent.LeftChild = None
        node.Parent = None
        node.LeftChild = None
        node.RightChild = None
        return True # если узел удален

    def __node_screening__(self, current_nodes: list, nodes: list):
        for node in current_nodes:
            if node is not None:
                nodes.append(node)
                nodes = self.__node_screening__([node.LeftChild, node.RightChild], nodes)
        return nodes

    def Count(self):
        count = len(self.__node_screening__([self.Root], [])) # количество узлов в дереве)
        return count

    def ListNodes(self):
        nodes = self.__node_screening__([self.Root], [])
        res = []
        for i in nodes:
            res.append(i.NodeValue)
        return res
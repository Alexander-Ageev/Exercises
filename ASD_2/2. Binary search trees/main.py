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
    """Класс описывает вспомогательную структуру с информацией о последней операции поиска"""
    def __init__(self):
        """
        Создает объект с информацией о результатах поиска
        self.Node = None - если в дереве нет узлов
        self.NodeHasKey = False - если узел не найден
        self.ToLeft = True - если родительскому узлу надо
        добавить новый узел левым потомком
        """
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False

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
        """Возвращает True, если удалось добавить новый элемент в дерево"""
        res = self.FindNodeByKey(key)
        if res.NodeHasKey is True:
            return False # если ключ уже есть
        if res.Node is None:
            self.Root = BSTNode(key, val, None)
        if res.ToLeft is True:
            res.Node.LeftChild = BSTNode(key, val, res.Node)
        if res.ToLeft is False:
            res.Node.RightChild = BSTNode(key, val, res.Node)
        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool):
        """
        Возвращает ссылку на узел с максимальным/минимальным значением ключа
        FindMax = True - поиск максимума
        FindMax = False - поиск минимума
        """
        if FindMax is True:
            if FromNode.RightChild is not None:
                return self.FinMinMax(FromNode.RightChild, FindMax)
            return FromNode
        if FromNode.LeftChild is not None:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        return FromNode

    def _ReplaceNode_(self, node: BSTNode, new_node: BSTNode):
        """
        Возвращает True, если удалось заменить node на new_node в дереве.
        Метод заменяет все взаимные связи как в узле-родителе, так и в узле-потомке.
        Для удаления листа нужно подать агрумент new_node = None
        """
        if node.Parent is None:
            self.Root = new_node
        elif node is node.Parent.LeftChild:
            node.Parent.LeftChild = new_node
        elif node is node.Parent.RightChild:
            node.Parent.RightChild = new_node
        if new_node is not None:
            new_node.Parent = node.Parent
            new_node.LeftChild = node.LeftChild
            new_node.RightChild = node.RightChild
            node_childs = self._GetChilds_(new_node)
            for i in node_childs:
                i.Parent = new_node
        return True

    def _ClearLink_(self, node: BSTNode):
        """Удаляет ссылки на родительский и дочерние узлы"""
        node.Parent = None
        node.LeftChild = None
        node.RightChild = None

    def _GetChilds_(self, node: BSTNode):
        """
        Возвращает список дочерних ненулевых узлов
        дочерние узлы отсутствуют - []
        есть только один узел - [узел]
        есть оба узла - [левый узел, правый узел]
        """
        res = []
        if node.LeftChild is not None:
            res.append(node.LeftChild)
        if node.RightChild is not None:
            res.append(node.RightChild)
        return res

    def DeleteNodeByKey(self, key):
        """Удаляет узел по заданному ключу. Возвращает True при успешном удалении"""
        node_info = self.FindNodeByKey(key)
        node = node_info.Node
        node_childs = self._GetChilds_(node)
        if node_info.NodeHasKey is False:
            return False
        #if node is self.Root and len(node_childs) > 0:
        #    return False
        if len(node_childs) == 0:
            replacement_node = None
        elif len(node_childs) == 1:
            replacement_node = node_childs[0]
            self._ReplaceNode_(replacement_node, None)
        elif len(node_childs) == 2:
            replacement_node = self.FinMinMax(node.RightChild, False)
            temp_childs = self._GetChilds_(replacement_node)
            self._ReplaceNode_(replacement_node, None)
            if len(temp_childs) == 1:
                node.RightChild = temp_childs[0]
        self._ReplaceNode_(node, replacement_node)
        self._ClearLink_(node)
        return True

    def Count(self):
        """Возвращает количество узлов в дереве"""
        count = len(self._NodeScreening_([self.Root], []))
        return count

    def _NodeScreening_(self, current_nodes: list, nodes: list):
        """Возвращает список узлов в дереве"""
        for node in current_nodes:
            if node is not None:
                nodes.append(node)
                nodes = self._NodeScreening_([node.LeftChild, node.RightChild], nodes)
        return nodes

    def ListNodes(self, mode = False):
        """Возвращает список значений всех узлов в дереве"""
        nodes = self._NodeScreening_([self.Root], [])
        res = []
        for i in nodes:
            if not mode:
                data = i.NodeValue
            else:
                if i.Parent is None:
                    parent = None
                else:
                    parent = i.Parent.NodeValue
                if i.LeftChild is None:
                    left_child = None
                else:
                    left_child = i.LeftChild.NodeValue
                if i.RightChild is None:
                    right_child = None
                else:
                    right_child = i.RightChild.NodeValue
                data = (parent, i.NodeValue, left_child, right_child)
            res.append(data)
        return res

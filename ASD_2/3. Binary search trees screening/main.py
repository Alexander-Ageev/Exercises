"""
Модуль содержит реализацию типа данных БИНАРНОЕ ДЕРЕВО ПОИСКА
а также реализацию методов обхода дерева в ширину и глубину
"""

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

    def _FindNode_(self, current_node: BSTNode, key):
        """Поиск узла по значению, либо родительского узла, куда необходимо значение добавить"""
        if current_node is None: #Ключ не найден, дошли до нижнего уровня дерева
            return self
        elif current_node.NodeKey == key: #Ключ найден
            self.NodeHasKey = True
            self.Node = current_node
            return self
        elif current_node.NodeKey > key: #Идем по левой ветви
            self.ToLeft = True
            next_node = current_node.LeftChild
        elif current_node.NodeKey < key: #Идем по право ветви
            self.ToLeft = False
            next_node = current_node.RightChild
        self.Node = current_node
        return self._FindNode_(next_node, key)

class BST:
    """Класс описывает структуру бинарного дереа поиска"""
    def __init__(self, node: BSTNode):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        """Возвращает ссылку на узел и сопутстующую информацтю поиска"""
        node_info = BSTFind()
        return node_info._FindNode_(self.Root, key)

    def AddKeyValue(self, key, val):
        """Возвращает True, если удалось добавить новый элемент в дерево"""
        node_info = self.FindNodeByKey(key)
        if node_info.NodeHasKey is True:
            return False # если ключ уже есть
        elif node_info.Node is None:
            self.Root = BSTNode(key, val, None)
        elif node_info.ToLeft is True:
            node_info.Node.LeftChild = BSTNode(key, val, node_info.Node)
        elif node_info.ToLeft is False:
            node_info.Node.RightChild = BSTNode(key, val, node_info.Node)
        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool):
        """
        Возвращает ссылку на узел с максимальным/минимальным значением ключа
        FindMax = True - поиск максимума
        FindMax = False - поиск минимума
        """
        if FindMax is True and FromNode.RightChild is not None:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        elif FindMax is True and FromNode.RightChild is None:
            return FromNode
        elif FindMax is False and FromNode.LeftChild is not None:
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
        if len(node_childs) == 0:
            replacement_node = None
        elif len(node_childs) == 1:
            replacement_node = node_childs[0]
            self._ReplaceNode_(replacement_node, None)
        elif len(node_childs) == 2:
            replacement_node = self.FinMinMax(node.RightChild, False)
            rep_node_childs = self._GetChilds_(replacement_node)
            self._ReplaceNode_(replacement_node, None)
            if len(rep_node_childs) == 1:
                node.RightChild = rep_node_childs[0]
        self._ReplaceNode_(node, replacement_node)
        self._ClearLink_(node)
        return True

    def Count(self):
        """Возвращает количество узлов в дереве"""
        count = len(self._in_order_screening_([self.Root], []))
        return count

    def _in_order_screening_(self, current_node: BSTNode, nodes: list):
        """Возвращает список узлов в дереве. In-Order"""
        if current_node.LeftChild is not None:
            nodes = self._in_order_screening_(current_node.LeftChild, nodes)
        nodes.append(current_node)
        if current_node.RightChild is not None:
            nodes = self._in_order_screening_(current_node.RightChild, nodes)
        return nodes


    def _post_order_screening_(self, current_node: BSTNode, nodes: list):
        """Возвращает список узлов в дереве. Post-order"""
        if current_node.LeftChild is not None:
            nodes = self._post_order_screening_(current_node.LeftChild, nodes)
        if current_node.RightChild is not None:
            nodes = self._post_order_screening_(current_node.RightChild, nodes)
        nodes.append(current_node)
        return nodes

    def _pre_order_screening_(self, current_node: BSTNode, nodes: list):
        """Возвращает список узлов в дереве. Pre-Order"""
        nodes.append(current_node)
        if current_node.LeftChild is not None:
            nodes = self._pre_order_screening_(current_node.LeftChild, nodes)
        if current_node.RightChild is not None:
            nodes = self._pre_order_screening_(current_node.RightChild, nodes)
        return nodes

    def DeepAllNodes(self, order: int):
        """
        Метод обхода дерева в глубину. Возвращает список элементов в порядке обхода:
        0 - In-Order
        1 - Post-Order
        2 - Pre-Order
        При некорректном аргументе order возвращает False
        """
        if order == 0:
            nodes = self._in_order_screening_(self.Root, [])
        elif order == 1:
            nodes = self._post_order_screening_(self.Root, [])
        elif order == 2:
            nodes = self._pre_order_screening_(self.Root, [])
        else:
            nodes = []
        return tuple(nodes)

    def _WideScreening_(self, root: list, nodes: list):
        new_nodes = []
        for node in root:
            if node.LeftChild is not None:
                new_nodes.append(node.LeftChild)
            if node.RightChild is not None:
                new_nodes.append(node.RightChild)
        nodes += new_nodes
        if len(new_nodes) > 0:
            self._WideScreening_(new_nodes, nodes)
        return nodes

    def WideAllNodes(self):
        nodes = self._WideScreening_([self.Root], [self.Root]) 
        return tuple(nodes)

    def ListNodes(self, nodes: tuple, detail = False):
        """
        Возвращает список значений всех узлов в дереве.
        detail - режим предоставления детальной информации
        """
        res = []
        for i in nodes:
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
            if detail:
                data = (parent, i.NodeValue, left_child, right_child)
            else:        
                data = i.NodeValue
            res.append(data)
        return res

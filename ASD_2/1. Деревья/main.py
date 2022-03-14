"""Модуль содержит реализацию типа данных ДЕРЕВЬЯ"""

class SimpleTreeNode:
    """Описание узла - базового элемента дерева"""

    def __init__(self, val, parent):
        """Инициализация узла"""
        self.node_value = val # значение в узле
        self.parent = parent # родитель или None для корня
        self.children = [] # список дочерних узлов

class SimpleTree:
    """
    Базовые операции взаимодействия с деревом:
    1. добавление узла
    2. удаление узла и его дочерних ветвей
    3. возвращение списка всех узлов
    4. поиск всех узлов по значению
    5. перемещение ветви новому родительскому узлу
    6. количество узлов в дереве
    7. количество листьев в дереве (лист - узел без дочерних ветвей)
    """
    def __init__(self, root):
        """Инициализация дерева"""
        self.root = root # корень, может быть None

    def __Getchildrens__(self, roots: list, nodes: list):
        """Возвращает список всех узлов, начиная с roots"""
        for i in roots:
            nodes.append(i)
            self.__Getchildrens__(i.children, nodes)
        return nodes

    def __FindValues__(self, roots: list, nodes: list, value):
        """Возвращает список всех узлов со значением value"""
        for i in roots:
            if i.node_value == value:
                nodes.append(i)
            self.__FindValues__(i.children, nodes, value)
        return nodes

    def __FindLeaf__(self, roots: list, nodes: list):
        for i in roots:
            if i.children == []:
                nodes.append(i)
            self.__FindLeaf__(i.children, nodes)
        return nodes

    def AddChild(self, parent_node: SimpleTreeNode, new_child: SimpleTreeNode):
        """Добавляет дочерний узел к parent_node"""
        parent_node.children.append(new_child)
        new_child.parent = parent_node
        return 0

    def DeleteNode(self, node_to_delete):
        """Удаляет узел вместе с дочерними ветвями"""
        if node_to_delete is not self.root:
            parent = node_to_delete.parent
            parent.children.remove(node_to_delete)
            #возможно, стоит рекурсивно обнулить взаимные ссылки на узлы удаляемой ветви
        return 0

    def GetAllNodes(self):
        """Возвращает список всех узлов дерева"""
        nodes = []
        return self.__Getchildrens__([self.root], nodes)

    def GetNodesValues(self, nodes):
        """Возвращает список значений всех узлов дерева"""
        values = [i.node_value for i in nodes]
        return values

    def FindNodesByValue(self, val):
        """Возвращает список узлов с заданным значением val"""
        nodes = []
        return self.__FindValues__([self.root], nodes, val)

    def MoveNode(self, original_node, new_parent):
        """Перемещает узел original_node вместе с его дочерними ветвями к родителю new_parent"""
        if original_node is not self.root:
            old_parent = original_node.parent
            old_parent.children.remove(original_node)
            original_node.parent = new_parent
            new_parent.children.append(original_node)
        return 0

    def Count(self):
        """Возвращает количество всех узлов в дереве"""
        return len(self.GetAllNodes())

    def LeafCount(self):
        """Возвращает количество всех листьев в дереве"""
        return len(self.__FindLeaf__([self.root], []))

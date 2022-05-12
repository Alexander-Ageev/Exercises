"""Модуль содержит реализацию типа данных ДЕРЕВЬЯ"""

class SimpleTreeNode:
    """Описание узла - базового элемента дерева"""

    def __init__(self, val, Parent):
        """Инициализация узла"""
        self.NodeValue = val # значение в узле
        self.Parent = Parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
        self.Level = -1

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
        self.Root = root # корень, может быть None

    def _GetChildrens_(self, roots: list, nodes: list):
        """Возвращает список всех узлов, начиная с roots"""
        for i in roots:
            nodes.append(i)
            self._GetChildrens_(i.Children, nodes)
        return nodes

    def _FindValues_(self, roots: list, nodes: list, value):
        """Возвращает список всех узлов со значением value"""
        for i in roots:
            if i.NodeValue == value:
                nodes.append(i)
            self._FindValues_(i.Children, nodes, value)
        return nodes

    def _FindLeaf_(self, roots: list, nodes: list):
        """Возвращает список всех листьев"""
        for i in roots:
            if i.Children == []:
                nodes.append(i)
            self._FindLeaf_(i.Children, nodes)
        return nodes

    def _SetLevel_(self, roots: list, Level):
        """Устанавливает уровень каждому узлу дерева"""
        for i in roots:
            i.Level = Level
            self._SetLevel_(i.Children, Level+1)

    def _GetLevel_(self, roots: list, nodes: list):
        """Возвращает список (Level, NodeValue), начиная с roots"""
        for i in roots:
            nodes.append((i.Level, i.NodeValue))
            self._GetLevel_(i.Children, nodes)
        return nodes

    def AddChild(self, Parent_node: SimpleTreeNode, new_child: SimpleTreeNode):
        """Добавляет дочерний узел к Parent_node"""
        if Parent_node is not None:
            Parent_node.Children.append(new_child)
            new_child.Parent = Parent_node
        return 0

    def DeleteNode(self, node_to_delete):
        """Удаляет узел вместе с дочерними ветвями"""
        if node_to_delete is not self.Root:
            Parent = node_to_delete.Parent
            Parent.Children.remove(node_to_delete)
            #возможно, стоит рекурсивно обнулить взаимные ссылки на узлы удаляемой ветви
        return 0

    def GetAllNodes(self):
        """Возвращает список всех узлов дерева"""
        return self._GetChildrens_([self.Root], [])

    def GetNodesValues(self, nodes):
        """Возвращает список значений всех узлов дерева"""
        values = [i.NodeValue for i in nodes]
        return values

    def FindNodesByValue(self, val):
        """Возвращает список узлов с заданным значением val"""
        return self._FindValues_([self.Root], [], val)

    def MoveNode(self, original_node, new_Parent):
        """Перемещает узел original_node вместе с его дочерними ветвями к родителю new_Parent"""
        if original_node is not self.Root:
            old_Parent = original_node.Parent
            old_Parent.Children.remove(original_node)
            original_node.Parent = new_Parent
            new_Parent.Children.append(original_node)
        return 0

    def Count(self):
        """Возвращает количество всех узлов в дереве"""
        return len(self.GetAllNodes())

    def LeafCount(self):
        """Возвращает количество всех листьев в дереве"""
        return len(self._FindLeaf_([self.Root], []))

    def SetLevel(self):
        """Инициализация _SetLevel_"""
        Level = 0
        self._SetLevel_([self.Root], Level)
        return 0

    def GetLevel(self):
        """Инициализация _GetLevel_"""
        res = self._GetLevel_([self.Root], [])
        res.sort()
        return res

    def CutEven(self, roots, edges):
        """Поиск ребер для удаления"""
        if roots == []:
            return edges
        parents = []
        for node in roots:
            nodes_count = len(self._GetChildrens_([node], []))
            if nodes_count % 2 == 0 and node.Parent is not None:
                edges.append(node.Parent)
                edges.append(node)
                node.Parent.Children.remove(node)
            if node.Parent is not None:
                parents.append(node.Parent)
        parents = list(set(parents))
        return self.CutEven(parents, edges)

    def EvenTrees(self):
        """
        Возвращает список вершин, ребра между которыми нужно удалить,
        чтобы получить лес из максимального количества четных деревьев.
        Список заполняется парами вершин по принципу: вершина родитель - вершина потомок
        """
        leafs = self._FindLeaf_([self.Root], [])
        leaf_parents = []
        for leaf in leafs:
            leaf_parents.append(leaf.Parent)
        leaf_parents = list(set(leaf_parents))
        edges = self.CutEven(leaf_parents, [])
        return edges

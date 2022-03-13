from tkinter.messagebox import NO


class SimpleTreeNode:
    """Описание узла - базового элемента дерева"""
    
    def __init__(self, val, parent):
        """Инициализация узла"""
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

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

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        """Добавляет дочерний узел к ParentNode"""
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        return 0

    def DeleteNode(self, NodeToDelete):
        """Удаляет узел вместе с дочерними ветвями"""
        parent = NodeToDelete.Parent
        parent.Childrens.remove(NodeToDelete)

    def __GetChildrens__(self, roots: list, nodes: list):
        """Возвращает список всех узлов, начиная с roots"""
        for i in roots:
            nodes.append(i)
            self.__get_childrens__(i.Children, nodes)
        return nodes

    def GetAllNodes(self):
        """Возвращает список всех узлов дерева"""
        return self.__get_childrens__([self.Root], [])

    def GetAllNodesValues(self):
        """Возвращает список значений всех узлов дерева"""
        nodes = self.GetAllNodes()
        values = [i.NodeValue for i in nodes]
        return values

    def FindNodesByValue(self, val):
        """Возвращает список узлов с заданным значением val"""
        # ваш код поиска узлов по значению
        return []
   
    def MoveNode(self, OriginalNode, NewParent):
        """Перемещает узел OriginalNode вместе с его дочерними ветвями к родителю NewParent"""
        # ваш код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        pass  
   
    def Count(self):
        """Возвращает количество всех узлов в дереве"""
        # количество всех узлов в дереве
        return 0

    def LeafCount(self):
        """Возвращает количество всех листьев в дереве"""
        # количество листьев в дереве
        return 0

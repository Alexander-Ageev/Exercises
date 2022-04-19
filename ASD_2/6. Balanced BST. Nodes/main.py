"""
Модуль описывает реализацию балансировки бинарного дерева поиска, 
реализованного через узлы
"""

class BSTNode:
    """Инициализация объекта Node - основного элемента дерева"""
    def __init__(self, key, parent):
        self.KeyNode = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        if self.Parent is None:
            self.Level = 0 # уровень узла
        else:
            self.Level = self.Parent.Level + 1

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
        elif current_node.KeyNode == key: #Ключ найден
            self.NodeHasKey = True
            self.Node = current_node
            return self
        elif current_node.KeyNode > key: #Идем по левой ветви
            self.ToLeft = True
            next_node = current_node.LeftChild
        elif current_node.KeyNode < key: #Идем по правой ветви
            self.ToLeft = False
            next_node = current_node.RightChild
        self.Node = current_node
        return self._FindNode_(next_node, key)

class BalancedBST:
    """Класс описывает метод создания сбалансированного дерева"""
    def __init__(self):
        self.Root = None # корень дерева

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
            self.Root = BSTNode(key, None)
        elif node_info.ToLeft is True:
            node_info.Node.LeftChild = BSTNode(key, node_info.Node)
        elif node_info.ToLeft is False:
            node_info.Node.RightChild = BSTNode(key, node_info.Node)
        return True

    def GetMiddleIndex(self, array: list):
        "Возвращает индекс середины массива. Если массив пустой - возвращает -1"
        size = len(array)
        if size == 0:
            mid_index = -1
        else:
            mid_index = size // 2
        return mid_index

    def _GenTree_(self, part_array: list):
        """
        Получает на вход отсортированный по возрастанию массив.
        Создает структуру сбалансированного дерева
        """
        new_parts = []
        for part in part_array:
            mid_index = self.GetMiddleIndex(part)
            if mid_index != -1:
                self.AddKeyValue(part[mid_index], part[mid_index])           
                left_branch = part[0: mid_index]
                right_branch = part[mid_index+1:]
                new_parts += [left_branch, right_branch]
        if new_parts != []:
            self._GenTree_(new_parts)
        return None

    def GenerateTree(self, a: list):
        """
        Инициализация GenTree:
        на вход метода поступает несортированный массив а
        """
        a.sort()
        self._GenTree_([a])
    
    def IsBalanced(self, root_node):
        if root_node






        return False # сбалансировано ли дерево с корнем root_node













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

    def ListNodes(self, detail = False):
        """
        Возвращает список значений всех узлов в дереве в порядке по уровням.
        Если detail = True, возвращает список кортежей с подробной информацией 
        о стуктуре дерева:
        1. Уровень узла
        2. Значение(ключ) родительского узла
        3. Значение(ключ) текущего узла
        4. Значение(ключ) левого потомка
        5. Значение(ключ) правого потомка
        """
        nodes = self._WideScreening_([self.Root], [self.Root])
        res = []
        for i in nodes:
            if i.Parent is None:
                parent = None
            else:
                parent = i.Parent.KeyNode
            if i.LeftChild is None:
                left_child = None
            else:
                left_child = i.LeftChild.KeyNode
            if i.RightChild is None:
                right_child = None
            else:
                right_child = i.RightChild.KeyNode
            if detail:
                data = (i.Level, parent, i.KeyNode, left_child, right_child)
            else:        
                data = i.KeyNode
            res.append(data)
        return res

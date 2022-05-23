"""Модуль описывает реализацию класса Simple Graph и метода обхода графа в глубину и ширину"""
class Vertex:
    """Класс описывает вершину графа. Вершина содержит информацию - абстрактное значение"""
    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:
    """
    Класс описывает структуру Sipmle Graph.
    Структура состоит из матрицы связей и списка вершин графа.
    Параметр v - индекс вершины в списке  vertex.
    """
    def __init__(self, size):
        """
        max_vertex - максимальное количество вершин в графе.
        Исходя из этого разера создается матрица связей.
        m_adjacency - Матрица связей вершин:
            0 - ребро между вершинами отсутствует;
            1 - вершины связаны.
        vertex - список вершин графа
        """
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, value):
        """Добавляет новую вершину со значением value в граф. Вершина добавляется без связей"""
        index = 0
        while self.vertex[index] is not None:
            index += 1
            if index >= self.max_vertex:
                return False
        self.vertex[index] = Vertex(value)
        return True

    def RemoveVertex(self, v):
        """Удаление вершины из графа"""
        if self.vertex[v] is not None:
            self.vertex[v] = None
            for i in range(self.max_vertex):
                self.RemoveEdge(i, v)
            return True
        return False

    def IsEdge(self, v1, v2):
        """Возвращает True, если вершина v1 соединена ребром с вершиной v2"""
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            return bool(self.m_adjacency[v1][v2])
        return False

    def AddEdge(self, v1, v2):
        """Добавление ребра между вершинами v1 и v2"""
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
            return True
        return False

    def RemoveEdge(self, v1, v2):
        """Удаление ребра между вершинами v1 и v2"""
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        return True

    def InitSearch(self):
        """Инициализация поиска в глубину - все вершины помечаются как непосещенные"""
        for vertex in self.vertex:
            vertex.Hit = False

    def GetAdjasentVertex(self, current_vertex_id: int):
        """Возвращает список индексов смежных вершин"""
        adjasent_vertex = []
        for i in range(len(self.m_adjacency[current_vertex_id])):
            if self.m_adjacency[current_vertex_id][i] == 1:
                adjasent_vertex.append(i)
        return adjasent_vertex

    def GetNotHitVertex(self, vertex_idx: list):
        """Возвращает индекс первой непосещенной вершины из списка"""
        for i in vertex_idx:
            if self.vertex[i].Hit is False:
                return i
        return None

    def DepthStep(self, current_vertex_id: int, search_vertex_id: int, stack: list):
        """
        Возвращает путь от заданной вершины до search_vertex_id в виде списка на объекты Vertex.
        Путь записывается в self.stack.
        Если вершины не соединены, возвращает пустой список.
        """
        if self.vertex[current_vertex_id].Hit is False:
            self.vertex[current_vertex_id].Hit = True
            stack.append(self.vertex[current_vertex_id])
        adjasent_vertex_idx = self.GetAdjasentVertex(current_vertex_id)
        new_vertex_id = self.GetNotHitVertex(adjasent_vertex_idx)
        if search_vertex_id in adjasent_vertex_idx:
            stack.append(self.vertex[search_vertex_id])
            return stack
        elif new_vertex_id is None and len(stack) > 1:
            stack.pop(-1)
            new_vertex_id = self.vertex.index(stack[-1])
        elif new_vertex_id is None and len(stack) <= 1:
            stack.pop(-1)
            return stack
        self.DepthStep(new_vertex_id, search_vertex_id, stack)
        return stack

    def DepthFirstSearch(self, VFrom: int, VTo: int):
        """
        Возвращает путь от вершины с индексом VFrom к вершине с индексом VTo.
        Путь представляет собой список элементов типа Vertex или пустой список,
        если вершины не связаны
        """
        self.InitSearch()
        return self.DepthStep(VFrom, VTo, [])


    def WidthStep(self, current_vertex_id: int, search_vertex_id: int, queue: list, buffer: list):
        self.vertex[current_vertex_id].Hit = True
        buffer.append(current_vertex_id)
        adjasent_vertex = self.GetAdjasentVertex(current_vertex_id)
        new_vertex_id = self.GetNotHitVertex(adjasent_vertex)
        if new_vertex_id == search_vertex_id:
            buffer.append(new_vertex_id)
            return buffer
        elif new_vertex_id is None and len(queue) > 1:
            queue.pop(0)
            buffer.pop(-1)
            new_vertex_id = self.vertex.index(queue[0])
        elif new_vertex_id is None and len(queue) <= 1:
            return []
        queue.append(self.vertex[new_vertex_id])
        self.vertex[new_vertex_id].Hit = True
        self.WidthStep(current_vertex_id, search_vertex_id, queue)
        return buffer


    def BreadthFirstSearch(self, VFrom, VTo):

        self.InitSearch()
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
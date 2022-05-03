"""Модуль описывает реализацию класса Simple Graph"""
class Vertex:
    """Класс описывает вершину графа. Вершина содержит информацию - абстрактное значение"""
    def __init__(self, val):
        self.Value = val
  
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

        m_adjacency - Матрица связей вершин. 0 - ребро между вершинами отсутствует; 1 - вершины связаны.
        vertex - список вершин графа
        """
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
    
    def AddVertex(self, value):
        """Добавляет новую вершину со значением value в граф. Вершина добавляется без связей"""
        index = 0
        while self.vertex != None:
            index += 1
            if index >= self.max_vertex:
                return False
        self.vertex[index] = Vertex[value]
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

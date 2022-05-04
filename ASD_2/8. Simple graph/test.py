"""Модуль содержит тесты для реализации класса Simple Graph"""
import unittest
from main import SimpleGraph

GRAPH_SIZE = 5
BASIC_MATRIX = [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0]
               ]

EMPTY_MATRIX = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
               ]

class MainTest(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(GRAPH_SIZE)
        for i in range(GRAPH_SIZE):
            vertex_val = i + 3
            self.graph.AddVertex(vertex_val)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(3, 4)

    def test_matrix(self):
        """Проверка исходной матрицы соответствия"""
        data = self.graph.m_adjacency
        res = BASIC_MATRIX
        self.assertEqual(data, res)

    def test_add_more_vertex(self):
        """
        Проверка на добавление вершин в граф.
        Добавляется большее количество вершин, чем помещается в графе.
        """
        data = (self.graph.AddVertex(10), self.graph.m_adjacency)
        res = (False, BASIC_MATRIX)
        self.assertEqual(data, res)

    def test_del_vertex(self):
        """
        Проверка на удаление вершины из графа.
        """
        data = []
        res = []
        vertex = [None] * GRAPH_SIZE
        for i in range(GRAPH_SIZE):
            data.append(self.graph.RemoveVertex(i))
            res.append(True)
        data = (data, self.graph.vertex, self.graph.m_adjacency)
        res = (res, vertex, EMPTY_MATRIX)
        self.assertEqual(data, res)

    def test_del_none_vertex(self):
        """
        Проверка на удаление несуществующей вершины из графа.
        """
        matrix = [
                    [0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0]
                 ]
        self.graph.RemoveVertex(3)
        data = (self.graph.RemoveVertex(3), self.graph.vertex[3], self.graph.m_adjacency)
        res = (False, None, matrix)
        self.assertEqual(data, res)

    def test_del_add_vertex(self):
        """
        Проверка на удаление вершины и добавление новой.
        """
        matrix = [
                    [0, 1, 1, 0, 0],
                    [1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 0, 0, 0]
                 ]
        self.graph.RemoveVertex(3)
        self.graph.AddVertex(10)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(3, 3)
        data = []
        for i in self.graph.vertex:
            data.append(i.Value)
        data = (data, self.graph.m_adjacency)
        res = ([3, 4, 5, 10, 7], matrix)
        self.assertEqual(data, res)

    def test_edge_exist(self):
        """Проверка на существование ребра между вершинами"""
        data = self.graph.IsEdge(3, 3)
        res = True
        self.assertEqual(data, res)

    def test_edge_not_exist(self):
        """Проверка на отсутствие ребра между вершинами"""
        data = self.graph.IsEdge(1, 1)
        res = False
        self.assertEqual(data, res)

    def test_add_alone_vertex(self):
        """
        Проверка на добавление вершины, которая не связана с другими.
        """
        matrix = [
                    [0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0]
                 ]
        self.graph.RemoveVertex(3)
        self.graph.AddVertex(10)
        data = []
        for i in self.graph.vertex:
            data.append(i.Value)
        data = (data, self.graph.m_adjacency)
        res = ([3, 4, 5, 10, 7], matrix)
        self.assertEqual(data, res)

    def test_add_edge(self):
        """
        Проверка на добавление ребра между вершинами.
        """
        matrix = [
                    [0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1],
                    [1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0]
                 ]
        self.graph.AddEdge(0, 4)
        data = self.graph.m_adjacency
        res = matrix
        self.assertEqual(data, res)

    def test_del_edge(self):
        """
        Проверка на удаление ребра между вершинами.
        """
        matrix = [
                    [0, 1, 1, 1, 0],
                    [1, 0, 0, 1, 1],
                    [1, 0, 0, 1, 0],
                    [1, 1, 1, 0, 1],
                    [0, 1, 0, 1, 0]
                 ]
        self.graph.RemoveEdge(3, 3)
        data = self.graph.m_adjacency
        res = matrix
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()

"""
Модуль содержит тесты для реализации поиска в ширину в Simple Graph
и нахождения кратчайшего пути между вершинами
"""
import unittest
from main import SimpleGraph

GRAPH_SIZE = 9
BASIC_MATRIX = [
                [0, 1, 0, 1, 1, 0, 0, 0 , 0],
                [1, 0, 0, 0, 0, 1, 0, 0 , 0],
                [0, 0, 0, 0, 0, 1, 0, 1 , 0],
                [1, 0, 0, 0, 1, 0, 1, 0 , 0],
                [1, 0, 0, 1, 0, 1, 1, 0 , 0],
                [0, 1, 1, 0, 1, 0, 0, 1 , 0],
                [0, 0, 0, 1, 1, 0, 0, 0 , 0],
                [0, 0, 1, 0, 0, 1, 0, 0 , 1],
                [0, 0, 0, 0, 0, 0, 0, 1 , 0],
               ]

BASIC_EDGES = [
                (0, 1), (0,3), (0, 4),
                (1, 5),
                (2, 5), (2, 7),
                (3, 4), (3, 6),
                (4, 6), (4, 5),
                (5, 7),
                (7, 8)
              ]

class MainTest(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(GRAPH_SIZE)
        for i in range(GRAPH_SIZE):
            vertex_val = i
            self.graph.AddVertex(vertex_val)
        for edge in BASIC_EDGES:
            v1, v2 = edge
            self.graph.AddEdge(v1, v2)

    def test_setup(self):
        data = self.graph.m_adjacency
        res = BASIC_MATRIX
        self.assertEqual(data, res)

    def test_GetTriangle_true(self):
        """Проверка метода обнаружения треуугольника"""
        data = self.graph._GetTriangle_(0)
        res = [0, 3, 4]
        self.assertEqual(res, data)

    def test_GetTriangle_false(self):
        """Проверка метода обнаружения треуугольника"""
        data = self.graph._GetTriangle_(1)
        res = []
        self.assertEqual(res, data)

    def test_weak_base(self):
        """Проверка метода обнаружения треуугольника"""
        data = self.graph.WeakVertices()
        res = [self.graph.vertex[1], self.graph.vertex[8]]
        self.assertEqual(res, data)

    def test_weak_none(self):
        """Проверка метода обнаружения треуугольника"""
        self.graph.RemoveVertex(1)
        self.graph.RemoveVertex(8)
        data = self.graph.WeakVertices()
        res = []
        self.assertEqual(res, data)




if __name__ == '__main__':
    unittest.main()

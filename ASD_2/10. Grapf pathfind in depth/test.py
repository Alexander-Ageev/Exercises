"""Модуль содержит тесты для реализации поиска в глубину в Simple Graph"""
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

    def test_get_adjasent_vertex(self):
        """Проверка метода возвращения индексов смежных вершин"""
        data = self.graph.GetAdjasentVertex(2)
        res = [0, 3]
        self.assertEqual(res, data)

    def test_adjasent_vertex(self):
        """Проверка поиска пути между смежными вершинами"""
        data = self.graph.DepthFirstSearch(0, 2)
        res = [self.graph.vertex[0], self.graph.vertex[2]]
        self.assertEqual(res, data)

    def test_far_vertex(self):
        """Проверка поиска пути между отдаленными вершинами"""
        self.graph.RemoveEdge(3, 3)
        data = self.graph.DepthFirstSearch(0, 4)
        res = [self.graph.vertex[0], self.graph.vertex[1], self.graph.vertex[4]]
        self.assertEqual(res, data)

    def test_no_path(self):
        """Проверка поиска пути между несвязанными вершинами"""
        self.graph.RemoveEdge(3, 3)
        self.graph.RemoveEdge(1, 4)
        self.graph.RemoveEdge(3, 4)
        data = self.graph.DepthFirstSearch(0, 4)
        res = []
        self.assertEqual(res, data)

if __name__ == '__main__':
    unittest.main()

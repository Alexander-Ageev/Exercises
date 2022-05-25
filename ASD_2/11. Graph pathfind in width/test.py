"""
Модуль содержит тесты для реализации поиска в ширину в Simple Graph
и нахождения кратчайшего пути между вершинами
"""
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

    def test_find_adjasent_vertex_path(self):
        """Проверка обнаружения соседних вершин"""
        data = self.graph.BreadthFirstSearch(0, 1)
        res = [self.graph.vertex[0], self.graph.vertex[1]]
        self.assertEqual(res, data)

    def test_find_short_path(self):
        """Проверка обнаружения короткого пути до соседних вершин"""
        data = self.graph.BreadthFirstSearch(0, 3)
        res = [self.graph.vertex[0], self.graph.vertex[3]]
        self.assertEqual(res, data)

    def test_find_far_vertex_path(self):
        """Проверка обнаружения вершин через одну"""
        data = self.graph.BreadthFirstSearch(2, 1)
        res =  [[self.graph.vertex[2], self.graph.vertex[0], self.graph.vertex[1]],
                [self.graph.vertex[2], self.graph.vertex[3], self.graph.vertex[1]]]
        self.assertIn(data, res)

    def test_find_none_path(self):
        """Проверка поиска пути для несвязанных вершин"""
        self.graph.RemoveEdge(1, 4)
        self.graph.RemoveEdge(3, 4)
        data = self.graph.BreadthFirstSearch(0, 4)
        res = []
        self.assertEqual(data, res)

    def test_find_long_path(self):
        """Проверка поиска длинного пути"""
        self.graph.RemoveEdge(0, 3)
        self.graph.RemoveEdge(0, 1)
        data = self.graph.BreadthFirstSearch(0, 4)
        res =  [self.graph.vertex[0], self.graph.vertex[2],
                self.graph.vertex[3], self.graph.vertex[4]]
        self.assertEqual(data, res)

if __name__ == '__main__':
    unittest.main()

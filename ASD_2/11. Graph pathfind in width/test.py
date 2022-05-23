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

    def test_get_adjasent_vertex(self):

        data = 
        res = 
        self.assertEqual(res, data)







if __name__ == '__main__':
    unittest.main()

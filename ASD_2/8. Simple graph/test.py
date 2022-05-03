"""Модуль содержит тесты для реализации класса Simple Graph"""
import unittest
import random as rnd
from main import Vertex, SimpleGraph

GRAPH_SIZE = 5

class MainTest(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(GRAPH_SIZE)
        self.graph.AddVertex(2)

    def test_add_vertex(self):
        g = SimpleGraph(3)
        g.AddVertex(1) 
        #res = self.graph.AddVertex(1)
        res = g.vertex[0].Value
        data = 1
        self.assertEqual(data, res)
'''
    def test_add_vertex(self):
        """Проверка на добавление вершин в граф"""
        vert = []
        add_ok = [True * GRAPH_SIZE] + [False]
        res = []
        for i in range(GRAPH_SIZE + 1):
            vertex_val = rnd.randint(0, 10)
            res.append(self.graph.AddVertex(vertex_val))
            vert.append(vertex_val)
        for i in self.graph.vertex:
            res.append(i.Value)
        data = add_ok + vert
        self.assertEqual(data, res)
'''

if __name__ == '__main__':
    unittest.main()

import unittest

from xceptions import *
from matrix import Matrix, Pattern, Edge

class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.matrix = Matrix(3)
        self.ADJ_GRAPH_3X3 = {
            1: [2, 4, 5, 6, 8],
            2: [1, 3, 4, 5, 6, 7, 9],
            3: [2, 4, 5, 6, 8],
            4: [1, 2, 3, 5, 7, 8, 9],
            5: [1, 2, 3, 4, 6, 7, 8, 9],
            6: [1, 2, 3, 5, 7, 8, 9],
            7: [2, 4, 5, 6, 8],
            8: [1, 3, 4, 5, 6, 7, 9],
            9: [2, 4, 5, 6, 8]
        }

    def test_create_matrix(self):
        self.assertEqual(self.matrix.adj_graph, self.ADJ_GRAPH_3X3)

    def test_valid_pattern_reuse(self):
        self.assertRaises(TooManyEdgeReused, self.matrix.check_pattern, 1, 2, 5, 4, 2, 1, 4, 2)


class TestEdge(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3)

    def test_create_edge(self):
        self.assertRaises(InvalidEdge, Edge, self.matrix, 1, 3)
        self.assertRaises(InvalidEdge, Edge, self.matrix, 1, 9)
        self.assertRaises(InvalidEdge, Edge, self.matrix, 1, 7)

    def test_edge_direction(self):
        edge = Edge(self.matrix, 1, 2)
        self.assertEqual(edge.get_tuple(), (1,2))
        self.assertNotEqual(edge.get_tuple(), (2,1))

    def test_edge_equality(self):
        edge12 = Edge(self.matrix, 1, 2)
        edge21 = Edge(self.matrix, 2, 1)
        assert(edge12 == edge21)

    def test_edge_path(self):
        edge12 = Edge(self.matrix, 1, 2)
        self.assertRaises(BrokenEdge, edge12.next_valid_edge, 1, 4)

    def test_edge_path2(self):
        edge12 = Edge(self.matrix, 1, 2)
        edge24 = Edge(self.matrix, 2, 4)

        next_edge = edge12.next_valid_edge(2, 4)
        assert(edge24 == next_edge)

class TestPattern(unittest.TestCase):

    def setUp(self):
        self.matrix = Matrix(3)

    def test_create_pattern(self):
        self.assertRaises(ShortPattern, self.matrix.check_pattern, 1, 2)
        self.assertRaises(ShortPattern, self.matrix.check_pattern, 1, 2, 3)

        self.assertRaises(InvalidEdge, self.matrix.check_pattern, 1, 2, 3, 9)
        self.assertRaises(RepeatedEdge, self.matrix.check_pattern, 1, 2, 1, 4)

    def test_create_pattern2(self):
        pattern = self.matrix.check_pattern(1, 2, 3, 4)

        edge12 = Edge(self.matrix, 1, 2)
        edge23 = Edge(self.matrix, 2, 3)
        edge34 = Edge(self.matrix, 3, 4)

        assert(pattern.get_edge_list() == [edge12, edge23, edge34])

    def test_add_edge_to_pattern(self):
        pattern = self.matrix.check_pattern(1, 2, 3, 4)

        self.assertRaises(InvalidEdge, pattern.add_edge, 4, 6)
        self.assertRaises(BrokenEdge, pattern.add_edge, 5, 6)

        pattern.add_edge(4, 5)
        assert(pattern.get_last_edge() == Edge(self.matrix, 4, 5))

    def test_pattern_length(self):
        nodes = [1, 2, 3, 4, 1, 2, 4, 5, 1, 6, 3, 5, 9, 8, 5, 6, 7, 2, 9, 4, 8, 6, 2, 5, 7, 8, 3]
        pattern = self.matrix.check_pattern(*nodes)
        assert(pattern.edge_count() == 26)

    def test_2x2_pattern_count(self):
        matrix = Matrix(2, 2)
        count, summary_counts = matrix.count_patterns()
        assert(count == 720)
        assert(summary_counts == {8: 120, 4: 48, 5: 96, 6: 168, 7: 288})


if __name__ == '__main__':
    unittest.main()

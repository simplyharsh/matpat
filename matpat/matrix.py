"""
Matrix Implementation File

"""

from xceptions import *
from edge import Edge
from pattern import Pattern

class Matrix:
    """
    Class Matrix.

    Intended to be initialized once with size dimenssions.

    """


    def __init__(self, m, n=None):
        """
        Generates matrix of m x n.

        Assumes a square matrix if n is not given.
        """
        self.m = m
        self.n = n = n or m
        self.__matrix_array = []
        self.adj_graph = {}

        matrix = self.__matrix_array = []
        for i in range(m):
            x = i*n+1
            matrix.append(range(x, x+n))

        self.fill_adjacent_graph()

    def fill_adjacent_graph(self):
        """
        Generates adjancency graph, required to validate the pattern paths
        """
        matrix = self.__matrix_array
        m, n = self.m, self.n

        graph = {}
        for i in range(m):
            for j in range(n):
                node = matrix[i][j]

                adj_list = []
                # getting row adjacent nodes
                if not j-1 < 0:
                    adj_list.append(matrix[i][j-1])
                if not j+1 >= n:
                    adj_list.append(matrix[i][j+1])


                for ii in range(m):
                    for jj in range(n):
                        # leaving out current row
                        if not ii == i:
                            if jj == j:
                                # getting column adjacent nodes
                                if (ii == i+1 or ii == i-1):
                                    adj_list.append(matrix[ii][jj])
                            else:
                                if (ii-jj == i-j) or (ii+jj == i+j):
                                    # getting diagonal adjacent nodes
                                    if (ii == i-1 or ii == i+1) and (jj == j-1 or jj == j+1):
                                        adj_list.append(matrix[ii][jj])
                                else :
                                    # rest all are reachable by long edges
                                    adj_list.append(matrix[ii][jj])

                graph[node] = sorted(adj_list)

        self.adj_graph = graph

    def valid_edge(self, startnode, endnode):
        """
        Returns an `Edge instance` if valid edge else raises exception.

        Class `Edge` validates itself against adjacency graph of matrix.
        """
        return Edge(self, startnode, endnode)

    def check_pattern(self, *args):
        """
        Returns an `Pattern instance` if valid pattern else raises exception.

        Class `Pattern` instantiation validates all the edges.
        """
        return Pattern(self, *args)

    def count_patterns(self):
        total_count = 0
        summary_counts = {}

        def summarize(correct_pattern):
            l = len(correct_pattern)
            summary_counts[l] = (summary_counts.get(l) or 0) + 1

        graph = self.adj_graph


        def get_count(node, pattern_so_far=[]):
            count = 0
            try_pattern = pattern_so_far+[node]
            try:
                self.check_pattern(*try_pattern)
            except (InvalidEdge, TooManyEdgeReused) as e1:
                return 0
            except ShortPattern as e2:
                pass
            else:
                count = count + 1
                summarize(try_pattern)

            for i in graph[node]:
                count = count + get_count(i, try_pattern)

            return count

        for node in graph:
            total_count = total_count + get_count(node, [])

        return total_count, summary_counts

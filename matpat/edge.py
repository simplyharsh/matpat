"""
Edge Implementation File
"""

from xceptions import *

class Edge:
    """
    Class Edge

    Intended to keep an encapsulations of nodes and matrix, for validations.
    Also acts as Factory for other valid edges, given the nodes

    """
    __tuple = None
    __matrix = None
    __startnode = None
    __endnode = None
    def __init__(self, matrix, startnode, endnode):
        """
        Requires Matrix and Two Nodes

        Validates if its valid edge, using the adjacency graph of matrix
        """
        from matrix import Matrix
        if not isinstance(matrix, Matrix):
            raise BadMatrix

        self.__matrix = matrix
        self.__startnode = startnode
        self.__endnode = endnode

        graph = matrix.adj_graph
        if startnode not in graph:
            raise InvalidEdge("Cannot find startnode %(st)s in (%(st)s, %(en)s)" % {'st': startnode, 'en': endnode})

        if endnode not in graph[startnode]:
            raise InvalidEdge("Cannot reach endnode %(en)s from %(st)s in (%(st)s, %(en)s)" % {'st': startnode, 'en': endnode})

        self.__tuple = (startnode, endnode)

    def next_valid_edge(self, startnode, endnode):
        """
        Raises exception if (startnode, endnode) cannot form a continous path, else returns a next Edge instance.
        """
        if not startnode == self.__endnode:
            raise BrokenEdge("Broken edge (%(st)s, %(en)s) from (%(st2)s, %(en2)s)" % {'st': startnode, 'en': endnode, 'st2': self.__startnode, 'en2': self.__endnode})
        elif endnode == self.__startnode:
            raise RepeatedEdge("Repeated edge (%(st)s, %(en)s) and (%(st2)s, %(en2)s) consecutively." % {'st': startnode, 'en': endnode, 'st2': self.__startnode, 'en2': self.__endnode})

        return Edge(self.__matrix, startnode, endnode)

    def get_startnode(self):
        return self.__startnode

    def get_endnode(self):
        return self.__endnode

    def get_tuple(self):
        return self.__tuple

    def __repr__(self):
        return 'Edge: %s -> %s' % (self.__startnode, self.__endnode)

    def __eq__(self, other):
        """
        Shallow equality check.

        Makes sure Edge (x, y) == Edge (y, x)
        """
        if not isinstance(other, Edge):
            return False

        return self.__tuple == other.__tuple or self.__tuple == other.__tuple[::-1]

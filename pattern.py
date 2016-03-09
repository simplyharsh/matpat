"""
Pattern Implementation


"""
from xceptions import *
from constants import MAX_EDGE_REUSE, MIN_NODES

class Pattern:
    """
    Class Pattern

    Intended to keep track of edges added while initialization.
    """

    def __init__(self, matrix, *args):
        """
        Requires matrix instance for which pattern is being generated.
        Enforces pattern to be initialized by atleast 4 nodes.

        Splits the arguments and adds them as edges.

        Raises exception of edges are not valid.

        """
        from matrix import Matrix
        if not isinstance(matrix, Matrix):
            raise BadMatrix

        self.__matrix = matrix
        self.__edge_list = []
        self.__edge_reused_count = 0
        self.__reused_edges = []

        l = len(args)
        if l < MIN_NODES:
            raise ShortPattern

        for i in range(l-1):
            self.add_edge(*args[i:i+2])

    def next_valid_edge(self, startnode, endnode):
        """
        Raises exception if (startnode, endnode) does not create a valid path,
        else returns a valid edge instance
        """
        last_edge = self.get_last_edge()
        if not last_edge:
            return self.__matrix.valid_edge(startnode, endnode)
        else:
            return last_edge.next_valid_edge(startnode, endnode)

    def add_edge(self, startnode, endnode):
        """
        Adds edge to the pattern

        Checks whether re-use of edges is in permissible limits
        """
        try:
            edge = self.next_valid_edge(startnode, endnode)
        except BrokenEdge, e:
            raise BrokenEdge("Cannot add (%s, %s) to %s" % (startnode, endnode, self))

        if edge in self.__edge_list:
            if self.__edge_reused_count + 1 > MAX_EDGE_REUSE:
                raise TooManyEdgeReused
            self.__edge_reused_count = self.__edge_reused_count + 1
            self.__reused_edges.append(edge)

        self.__edge_list.append(edge)

    def edge_count(self):
        """
        Returns count of edges in this pattern
        """
        return len(self.__edge_list)

    def node_count(self):
        """
        Returns count of nodes in this pattern
        """
        return self.edge_count + 1

    def get_last_edge(self):
        """
        Returns last edge in this pattern

        Used to check next valid edge
        """
        if self.__edge_list:
            return self.__edge_list[::-1][0]
        return None

    def get_edge_list(self):
        """
        Returns list of added edges
        """
        return self.__edge_list

    def get_reused_edges(self):
        """
        Returns list of reused edges
        """
        return self.__reused_edges

    def __repr__(self):
        if not self.__edge_list:
            return 'Empty Pattern'

        s = self.__edge_list[0].get_startnode()
        for edge in self.__edge_list:
            s = "%s -> %s" % (s, edge.get_endnode())

        return "Pattern [%s]" % s

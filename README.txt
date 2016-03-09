Implements an android pattern-lock like architecture, that can be further extended with with new rules.

Rules for this :

    01. An acceptable pattern must touch atleast 4 points
    02. Only one edge re-use is allowed in one pattern
    03. {1, 2} {5, 9} is an edge. I have taken {1, 6} as a valid edge too.
    04. Edge {1,2} & {2,1} cannot come consecutively, as it would be like going to & fro.
    05. {1,3} {1,7} & {1,9} is not a valid edge, as they cannot be joined without passing through point 2, 4 and 5 respectively.

Hints:
    1              2              3
    4              5              6
    7              8              9

    Then connection between 1 & 2 is an edge ({5,9} is also an edge … and so on)
    1,2,4,5,2,1 is an acceptable pattern (connection between 1 & 2 has been used twice), however, 1,2,4,5,2,1,4,2 isn’t as connections between 1,2 & 4,2 have been used twice.


Usage:

    $ matrix = Matrix(3) # or matrix = Matrix(3, 3)
    $ nodes = [1,2,4,5,2,1]
    $ pattern = matrix.check_pattern(*nodes)
    $ pattern.add_edge(1, 4)
    $ pattern.add_edge(4, 2) # Raises TooManyEdgeReused exception

    $ nodes = [1,2,4,5,2,1, 4, 2]
    $ pattern = matrix.check_pattern(*nodes) # Raises TooManyEdgeReused exception

    $ nodes = [1, 2, 3, 4, 1, 2, 4, 5, 1, 6, 3, 5, 9, 8, 5, 6, 7, 2, 9, 4, 8, 6, 2, 5, 7, 8, 3]
    $ pattern = matrix.check_pattern(*nodes)

    $ matrix = Matrix(2, 2)
    $ count, summary_counts = matrix.count_patterns()


Tests:

Run tests.
python matpat/tests.py

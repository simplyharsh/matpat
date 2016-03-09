"""
Exceptions used in the package
"""

from constants import MAX_EDGE_REUSE

class CoreException(Exception):
    def __init__(self, message=None, *args, **kwargs):
        message = message or getattr(self, '__msg__', 'No message provided')
        Exception.__init__(self, message, *args, **kwargs)

class BadMatrix(CoreException):
    __msg__ = 'matrix should be instance of class Matrix'

class ShortPattern(CoreException):
    __msg__ = 'Pattern should touch atleast 4 nodes'

class InvalidEdge(CoreException):
    __msg__ = 'Invalid Edge'

class BrokenEdge(InvalidEdge):
    __msg__ = 'Broken Edge'

class RepeatedEdge(InvalidEdge):
    __msg__ = 'Not allowed. Repeated same edge in continuation.'

class TooManyEdgeReused(CoreException):
    __msg__ = "Maximum allowed reuse of edge is: %s" % MAX_EDGE_REUSE

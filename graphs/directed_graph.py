#!/usr/local/bin/python3
"""
# Directed Graph class using an Adjacency list representation
"""
class DirectedGraph:

  class Vertex:
    """Nested class representing an graph vertex"""
    __slots__ = 'element', 'discovered'

    def __init__(self, element):
      self.element = element
      self.discovered = False

    def get_element(self):
      return self.element

    def set_discover(self):
      self.discovered = True

    def is_discovered(self):
      return self.discovered


  class Edge:
    """Nested class representing a graph edge"""
    __slots__ = 'weigth', 'origin', 'destination'

    def __init__(self, u, v, w):
      self.origin = u
      self.destination = v
      self.weigth = w

    def endpoints(self):
      return (self.origin, self.destination)

    def opposite(self, v):
      if v is self.origin:
        return self.destination
      elif v is self.destination:
        return self.origin
      else:
        raise ValueError('vertex does not have an edge')

    def get_weight(self):
      return self.weigth


  def __init__(self):
    self._v_count = 0
    self._e_count = 0
    self.Adj = []


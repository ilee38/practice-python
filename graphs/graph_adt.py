#!/usr/local/bin/python3
"""
# General graph ADT class using an Adjacency list representation.
# An undirected or directed graph can be created by seting the type parameter.
"""
class Graph:

  class Vertex:
    """Nested class representing an graph vertex"""
    __slots__ = 'element'

    def __init__(self, element):
      self.element = element

    def get_element(self):
      return self.element


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


  def __init__(self, directed=False):
    self.directed = directed
    self._v_count = 0
    self._e_count = 0
    self.Adj = {}     #dictionary mapping vertices to edge lists


  def vertex_count(self):
    return self._v_count


  def edge_count(self):
    return self._e_count


  def insert_vertex(self, label):
    v = self.Vertex(label)
    self.Adj[v] = []
    self._v_count += 1
    return v


  def insert_edge(self, u, v, w):
    e = self.Edge(u, v, w)
    if u in self.Adj:
      self.Adj[u].append(e)
    else:
      self.Adj[u] = [e]
    self._e_count += 1

    if not self.directed:
      be = self.Edge(v, u, w)
      if v in self.Adj:
        self.Adj[v].append(be)
      else:
        self.Adj[v] = [be]
      self._e_count += 1

    return e
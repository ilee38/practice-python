#!/usr/local/bin/python3

class Graph:
  """ General graph ADT class using an Adjacency list representation.
      Either directed or undirected graphs can be created.

      Parameters:
      directed - boolean value indicating if graph is directed or undirected,
                 set to False by default.
  """


  class Vertex:
    """Nested class representing an graph vertex.
       parameters:
       element - is a label or name asociated with the vertex
       d - represents the current distance value during a graph exploration. Initially
       set to infinity.
       parent - the parent of the element during the graph exploration
    """
    __slots__ = 'element', 'd', 'parent'

    def __init__(self, element, d=float('inf')):
      self.element = element
      self.d = d
      self.parent = None

    def get_element(self):
      return self.element

    def get_d_val(self):
      return self.d

    def set_d_val(self, d):
      self.d = d

    def set_parent(self, p):
      self.parent = p

    def get_parent(self):
      return self.parent


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
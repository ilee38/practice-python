#!/usr/local/bin/python3
"""
# Directed Graph class using an Adjacency list representation
"""
from collections import deque

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
    return e


  def BFS(self, s):
    """ Performs breadth-first search on the graph, starting from vertex s.
        Returns a dict containing the discovery edges mapped as:
        {destination : source}
    """
    Q = deque()     #queue data structure to perform the BFS traversal
    discover_path = {}
    Q.append(s)
    while len(Q) > 0:
      v = Q.popleft()
      for e in self.Adj[v]:
        if e.opposite(v).get_element() not in discover_path:
          Q.append(e.opposite(v))
          discover_path[e.opposite(v).get_element()] = v.get_element()
    return discover_path


  def DFS(self, s):
    """ Performs Depth-first search on the graph, starting from vertex s.
        returns a dict containing the edges in the discovery path as:
        {destination : source}
    """
    visited = {}
    return self.DFS_visit(visited, s)


  def DFS_visit(self, visited, s):
    """ Performs the recursive depth-first search for the DFS method
    """
    for e in self.Adj[s]:
      if e.opposite(s).get_element() not in visited:
        visited[e.opposite(s).get_element()] = s.get_element()
        self.DFS_visit(visited, e.opposite(s))
    return visited


  def fill_endpoints(self, e):
    """ Returns a tuple containing the element values of the source and
        destination vertices in an edge e.
    """
    u, v = e.endpoints()
    return (u.get_element(), v.get_element())



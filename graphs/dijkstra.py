#!/usr/local/bin/python3

from priority_queue import *
from graph_adt import *

def dijkstra(G, s):
  """ Performs Dijktra's algorithm to find the shortest path from a single source
      to all other vertices in a weighted graph.

      Parameters:
      G - Graph represented with an adjacency list mapping the vertices to lists of edges
      s - source vertex

      Returns:
      A list of tuples representing the parent child relationships during the
      discovery paths. I.e. tuple = (parent, child)
  """
  q_cap = G.vertex_count() + G.edge_count()    #capacity of the priority queue
  S = []
  Q = PriorityQueue(q_cap)
  s.set_d_val(0)  #initialize source's current distance
  Q.insert(0, s)
  while not Q.is_empty() :
    min_element = Q.extract_min()
    u = min_element.get_value()
    if u not in S:
      S.append(u)
      for e in G.Adj[u]:
        priority, v = relax(u, e.opposite(u), e.get_weight())
        if priority and v:
          Q.insert(priority, v)
  return S


def relax(u, v, w):
  """ Performs edge relaxation during Dijktra's exploration

      Parameters:
      u - source node
      v - destination node
      w - weight from u to v

      Returns:
      tuple: (updated weight, v), if relaxation was performed.
             v is updated with its new parent.
  """
  if v.get_d_val() > (u.get_d_val() + w):
    v.set_d_val(u.get_d_val() + w)
    v.set_parent(u)    #make u the parent of v
    return(v.get_d_val(), v)
  else:
    return (None, None)


def main():
  #Instantiate undirected graph
  Gr = Graph()

  #Create vertices
  W = Gr.insert_vertex("w")
  P = Gr.insert_vertex("p")
  Y = Gr.insert_vertex("y")
  R = Gr.insert_vertex("r")
  B = Gr.insert_vertex("b")

  #Create edges
  W_P = Gr.insert_edge(W, P, 7)
  W_Y = Gr.insert_edge(W, Y, 19)
  P_Y = Gr.insert_edge(P, Y, 11)
  P_R = Gr.insert_edge(P, R, 15)
  P_B = Gr.insert_edge(P, B, 5)
  Y_R = Gr.insert_edge(Y, R, 4)
  B_R = Gr.insert_edge(B, R, 13)

  print("Number of vertices: ", Gr.vertex_count())
  print("Number of edges: ", Gr.edge_count())

  paths = dijkstra(Gr, R)
  print("Shortest paths (parent, destination):")
  for node in paths:
    parent = node.get_parent().get_element() if node.get_parent() is not None else None
    print(parent, ", ", node.get_element())

if __name__ == '__main__':
  main()
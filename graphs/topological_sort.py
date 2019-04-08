#!/usr/bin/env python3

from directed_graph import *

"""
   1. find any cycles on the DIRECTED graph (to determine if it is a DAG)
        - during DFS, if ANY node is visited more than once, then there's a cycle,
          so we break out of the traversal.
   2. if there's any cycles, no topological sort exists
   3. otherwise perform DFS and return the vertices in the reverse order in which
      they were visited
"""

def topological_sort(G, s):
  """ Performs topological sort on a directed graph if no cycles exist.

      Parameters:
      G - directed graph represented with an adjacency list
      s - starting vertex on the graph

      Returns:
      A list of edges in topological order if it exists, None otherwise
  """
  visited = [s.get_element()]
  cycle_counter = 0
  DFS(G, s, visited, cycle_counter)
  visited.reverse()
  return visited if not cycle_counter else None


def DFS(G, s, visited, cycle_counter):
  for e in G.Adj[s]:
    if e.opposite(s).get_element() not in visited:
      visited.append(e.opposite(s).get_element())
      DFS(G, e.opposite(s), visited, cycle_counter)
    else:
      cycle_counter += 1
      return

def main():
  DG = DirectedGraph()

  #Create vertices
  U = DG.insert_vertex("u")
  V = DG.insert_vertex("v")
  W = DG.insert_vertex("w")
  X = DG.insert_vertex("x")
  Y = DG.insert_vertex("y")
  Z = DG.insert_vertex("z")

  #Create edges
  U_V = DG.insert_edge(U, V, 0)
  #U_W = DG.insert_edge(U, W, 0)
  U_X = DG.insert_edge(U, X, 0)
  V_W = DG.insert_edge(V, W, 0)
  W_U = DG.insert_edge(W, U, 0)
  W_X = DG.insert_edge(W, X, 0)
  W_Y = DG.insert_edge(W, Y, 0)
  W_Z = DG.insert_edge(W, Z, 0)
  print("Number of vertices: ", DG.vertex_count())
  print("Number of edges: ", DG.edge_count())
  print("")

  topological_order = topological_sort(DG, U)
  print("Topological order:")
  if topological_order is not None:
    print(topological_order)
  else:
    print("no topological order exist in this graph")


if __name__ == '__main__':
  main()
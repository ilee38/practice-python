#!/usr/bin/env python3

from directed_graph import *

def topological_sort(G):
  """ Performs topological sort on a directed graph if no cycles exist.

      Parameters:
      G - directed graph represented with an adjacency list

      Returns:
      returns a dict containing the edges in the discovery path as:
        {destination : source}
  """
  if not has_cycles(G):
    dfs_visit = G.DFS()
    return dfs_visit
  else:
    print("Graph has cycles")
    return None


def has_cycles(G):
  """ Checks for cycles in a directed graph

      parameters:
      G - a directed graph represented with an adjacency list

      returns:
      boolean value indicating wether there was a cycle in the graph
  """
  cycles = False
  STARTED = 1
  FINISHED = 2
  for v in G.Adj:
    visited = {}
    to_finish = [v]
    while to_finish and not cycles:
      v = to_finish.pop()
      if v in visited:
        if visited[v] == STARTED:
          visited[v] = FINISHED
      else:
        visited[v] = STARTED
        to_finish.append(v)   #v has been started, but not finished yet

      for e in G.Adj[v]:
        if e.opposite(v) in visited:
          if visited[e.opposite(v)] == STARTED:
            cycles = True
        else:
          to_finish.append(e.opposite(v))
      if cycles:
        break
  return cycles


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
  U_W = DG.insert_edge(U, W, 0)
  U_X = DG.insert_edge(U, X, 0)
  V_W = DG.insert_edge(V, W, 0)
  #W_U = DG.insert_edge(W, U, 0)
  W_X = DG.insert_edge(W, X, 0)
  W_Y = DG.insert_edge(W, Y, 0)
  W_Z = DG.insert_edge(W, Z, 0)
  print("Number of vertices: ", DG.vertex_count())
  print("Number of edges: ", DG.edge_count())
  print("")

  topological_order = topological_sort(DG)
  print("Topological order:")
  print(topological_order)


if __name__ == '__main__':
  main()
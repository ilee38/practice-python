#!/usr/local/bin/python3

from directed_graph import DirectedGraph

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
  W_X = DG.insert_edge(W, X, 0)
  W_Y = DG.insert_edge(W, Y, 0)
  W_Z = DG.insert_edge(W, Z, 0)
  print("Number of vertices: ", DG.vertex_count())
  print("Number of edges: ", DG.edge_count())
  print("")

  bfs_path = DG.BFS(U)
  print("BFS discovery path {'destination' : 'source'} ")
  print(bfs_path)
  print("")
  dfs_path = DG.DFS(U)
  print("DFS discovery path {'destination' : 'source'} ")
  print(dfs_path)

if __name__ == '__main__':
  main()
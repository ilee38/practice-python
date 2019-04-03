#!/usr/local/bin/python3

import queue
from graph_adt import Graph

def dijkstra(G, s):


def main():
  #Create undirected graph instance
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
  R_B = Gr.insert_edge(R, B, 13)

  print("Number of vertices: ", Gr.vertex_count())
  print("Number of edges: ", Gr.edge_count())
  print("")


if __name__ == '__main__':
  main()
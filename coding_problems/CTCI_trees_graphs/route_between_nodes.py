#!/usr/bin/env python3
""" Problem 4.1 from the CtCI book
"""
from collections import deque

def found_route(G, u, v):
  """
    Implements Breadth-First Search to find a (shortest) route between two nodes.
    Returns True if there is a route between u and v in graph G,
    False otherwise.
    Assume G is an adjacency list representation of a graph (using a dict)
  """
  if G is None or u is None or v is None:
    return False
  visited = []
  Q = deque()
  Q.append(u)
  visited.append(u)
  while len(Q) != 0:
    elem = Q.popleft()
    for node in G[elem]:
      if node == v:
        return True
      if node not in visited:
        Q.append(node)
        visited.append(node)
  return False


def main():
  G = {'a':['b','c'], 'b':['c'], 'c':['d'], 'd':['b']}
  H = {'a':['b','c'], 'b':['d'], 'c':['d'], 'd':[], 'e':['c']}
  print(found_route(G, 'a', 'd'))
  print(found_route(H, 'a', 'e'))


if __name__ == '__main__':
  main()
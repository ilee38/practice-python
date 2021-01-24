#!/usr/bin/env python3

""" Implementation of Depth First Search to find a route between nodes
"""
from collections import deque

def find_route(graph, start, end):
   visited = set()
   Q = deque()
   Q.append(start)
   while Q:
      node = Q.popleft()
      if node not in visited:
         visited.add(node)
         if node == end:
            return True
      Q += graph[node]
   return False


def main():
   graph = {}
   graph['a'] = ['b', 'c', 'd']
   graph['b'] = ['c']
   graph['c'] = []
   graph['d'] = ['e']
   graph['e'] = []
   route = find_route(graph, 'a', 'e')
   print(route)
   route = find_route(graph, 'c', 'e')
   print(route)

if __name__ == '__main__':
   main()


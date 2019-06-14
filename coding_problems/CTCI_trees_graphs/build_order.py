#!/usr/bin/env python3

""" Problem 4.7 on CtCI book
"""
def make_graph(proj_list, dep_list):
  G = {}
  for i in range(len(proj_list)):
	  G[proj_list[i]] = []
  for j in range(len(dep_list)):
	  k,v = dep_list[j]
	  G[k].append(v)
  return G

def order(G):
	visited = []
	for v in G:
		if v not in visited:
			DFS_visit(G, v, visited)
	return reversed(visited)

def DFS_visit(G, v, visited):
	for elem in G[v]:
		if elem not in visited:
			DFS_visit(G, elem, visited)
	visited.append(v)



def main():
  p = ['a', 'b','c', 'd', 'e', 'f']
  dep = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
  g = make_graph(p, dep)
  ordering = order(g)
  for x in ordering:
    print(x)

if __name__ == '__main__':
  main()
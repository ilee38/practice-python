#!/usr/bin/env python3
""" Problem 4.3 from CtCI book
"""

def list_of_depths(root):
  if root is None:
    return None
  depth_lists = {}
  depth = 0
  dfs_visit(root, depth, depth_lists)
  return depth_lists

def dfs_visit(root, depth, depth_lists):
  if depth not in depth_lists:
    depth_lists[depth] = [root.val]
  else:
    depth_lists[depth].append(root.val)

  if root.left is not None:
    dfs_visit(root.left, depth+1, depth_lists)
  if root.right is not None:
    dfs_visit(root.right, depth+1, depth_lists)


class TreeNode:
  """ Class representing a node of the binary tree
  """
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def main():
  root = TreeNode('a')
  b = TreeNode('b')
  c = TreeNode('c')
  d = TreeNode('d')
  e = TreeNode('e')
  f = TreeNode('f')
  g = TreeNode('g')
  h = TreeNode('h')
  i = TreeNode('i')
  j = TreeNode('j')
  root.left = b
  root.right = c
  b.left = d
  b.right = e
  d.left = h
  e.right = i
  c.left = f
  c.right = g
  f.left = j
  lists = list_of_depths(root)
  for l in lists:
    print('depth ', l, ': ', lists[l])

if __name__ == '__main__':
  main()
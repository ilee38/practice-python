#!/usr/bin/env python3

""" Problem 4.2 on CtCI book
"""
from collections import deque

class MinBST:

  class Node:
    def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

  def __init__(self, Arr):
    self.Arr = Arr
    self.root = None

  def make_BST(self):
    n = len(self.Arr)
    Q = deque()
    self.root = self.Node(self.Arr[n//2])
    left_idx = (n//2)-1
    right_idx = (n//2)+1

    Q.append(self.root)
    while left_idx >= 0 and right_idx < n:
      curr_root = Q.popleft()
      curr_root.left = self.Node(self.Arr[left_idx])
      curr_root.right = self.Node(self.Arr[right_idx])
      Q.append(curr_root.left)
      Q.append(curr_root.right)
      left_idx -= 1
      right_idx += 1

    if left_idx == 0:
      curr_root = Q.popleft()
      curr_root.left = self.Node(self.Arr[0])
    elif right_idx == n-1:
      curr_root = Q.popleft()
      curr_root.right = self.Node(self.Arr[n-1])



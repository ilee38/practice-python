#!/usr/bin/env python3
""" Problem 4.4 from CtCI book
"""
import math

def is_balanced(root):
  return check_balanced(root) != -math.inf

def check_balanced(root):
  if root is None:
    return -1

  height_l = check_balanced(root.left)
  if height_l == -math.inf:
    return -math.inf

  height_r = check_balanced(root.right)
  if height_r == -math.inf:
    return -math.inf

  diff = abs(height_l - height_r)
  if diff > 1:
    return -math.inf
  else:
    return max(height_l, height_r) + 1
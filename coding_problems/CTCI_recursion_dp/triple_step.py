#!/usr/bin/env python3
""" Problem 8.1 from CtCI book
"""
def count_ways(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1

  counts = {1:1, 2:2, 3:4}
  curr_sum = 0
  for i in range(4, n+1):
    for j in range(1,i):
      curr_sum += counts[j]
    counts[i] = curr_sum
    curr_sum = 0
  return counts[n]
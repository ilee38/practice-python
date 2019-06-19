#!/usr/bin/env python3

""" Problem 5.1 in the CtCI book
"""
def bitwise_insertion(N, M, i, j, size_of_N):
  left_mask = ((1<<(size_of_N - (j+1))-1)) << (j+1) #need to know the size of N, i.e. # of bits in N,
  right_mask = (1<<i) - 1                           #in order to know how many 1's we need after position j
  mask = left_mask | right_mask
  N = N & mask
  M = M << i
  N = N | M
  return N
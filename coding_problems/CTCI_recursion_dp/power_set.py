#!/usr/bin/env python3
""" Problem 8.4 from CtCI book
"""
def power_set(S):
  find_subsets('', S)

def find_subsets(so_far, rest):
  if len(rest) == 0:
    print(so_far)
  else:
    _next = so_far + rest[0]          #take 1st element
    find_subsets(_next, rest[1:])     #include it in the set and recur w/out it
    find_subsets(so_far, rest[1:])    #don't include in the set and recur w/out it

#!/usr/bin/env python3
""" Problem 10.4 from CtCI book
"""

def search_no_size(A, x):
  if A is None or x is None:
    return None
  hi = find_hi(A)
  return _search(A, 0, hi, x)

def find_hi(A):
  hi = 1
  while A[hi] != -1:
    hi *= 2
  return hi

def _search(A, lo, hi, x):
  if lo > hi:
    return None
  mid = (hi + lo) // 2
  if A[mid] == x:
    return mid
  elif A[mid] == -1 or A[mid] > x:
    return _search(A, lo, mid-1, x)
  else:
    return _search(A, mid+1, hi, x)
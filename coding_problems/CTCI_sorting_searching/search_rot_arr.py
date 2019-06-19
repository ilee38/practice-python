#!/usr/bin/env python3

""" Problem 10.3 in CtCI book
"""
def search_rot(A, val):
  lo = 0
  hi = len(A)-1
  bin_search(A, lo, hi, val)

def bin_search(A, lo, hi, val):
  mid = (lo + hi) // 2
  if lo >= hi:
    print('None')   #value not found
    return
  if A[mid] == val:
    print(mid)
    return
  elif A[mid+1] == val:
    print(mid+1)
    return
  elif A[lo] < A[mid]:
    if val < A[mid] and val >= A[lo]:
      bin_search(A, lo, mid, val)
    else:
      bin_search(A, mid+1, hi, val)
  elif A[lo] > A[mid]:
    if val > A[mid] and val <= A[hi]:
      bin_search(A, mid+1, hi, val)
    else:
      bin_search(A, lo, mid, val)
  else:
    bin_search(A, lo, mid, val)
    bin_search(A, mid+1, hi, val)
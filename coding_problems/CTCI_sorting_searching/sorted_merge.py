#!/usr/bin/env python3

""" Problem 10.1 from CtCI book
"""
def sorted_merge(A, A_sz, B, B_sz):
  """ args:
        A_sz = number of elements in A
        B_sz = number of elements in B
  """
  a_last = A_sz-1
  b_last = B_sz-1
  buff_last = a_last + len(B)

  while a_last >= 0 and b_last >= 0:
    if B[b_last] >= A[a_last]:
      A[buff_last] = B[b_last]
      b_last -= 1
    else:
      A[buff_last] = A[a_last]
      a_last -= 1
    buff_last -= 1

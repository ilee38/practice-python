#!/usr/bin/env python3
""" Problem 8.3 from CtCI book
"""
def find_magic_index(A):
  if len(A) == 0 or A is None:
    return None
  lo = 0
  hi = len(A)-1
  return _find_index(A, lo, hi)


def find_index(A, lo, hi):
  """ finds the magic index for a sorted array of
      distinct integers
  """
  if lo > hi:
    return None
  mid = (hi + lo) // 2
  if A[mid] == mid:
    return mid
  elif A[mid] > mid:
    return find_index(A, lo, mid-1)
  else:
    return find_index(A, mid+1, hi)


def _find_index(A, lo, hi):
  """ finds the magic index for a sorted array where
      integers are NOT distinct
  """
  if lo > hi:
    return None
  mid = (hi + lo) // 2

  if A[mid] == mid:
    return mid

  left_idx = min(A[mid], mid-1)
  left = _find_index(A, lo, left_idx)
  if left is not None:
    return left

  right_idx = max(A[mid], mid+1)
  right = _find_index(A, right_idx, hi)
  return right
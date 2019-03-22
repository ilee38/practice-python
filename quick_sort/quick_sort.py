#!/usr/local/bin/python3
"""
# Implementation of the Quick-sort algorithm in-place
"""
import random

def _qs_partition(A, lo, hi):
  """ Performs the partitioning for Quick-sort. It does 3-way partitioning
   in-place (Sedgewick's method).
   Parameters:
   -------------
   A: list of elements
   lo: index of the 1st element
   hi: index of the last element
  """
  if lo >= hi:
    return
  lt = lo     #index of right-most element less than the pivot
  gt = hi     #index of left-most element greater than the pivot
  i = lo
  v = A[lo]     #pivot element, we always choose the 1st since the array is already shuffled
  while i <= gt:
    if A[i] < v:
      A[i], A[lt] = A[lt], A[i]   #swap the elements
      i += 1
      lt += 1
    elif A[i] > v:
      A[i], A[gt] = A[gt], A[i]   #swap the elements
      gt -= 1
    else:
      i += 1
  _qs_partition(A, lo, lt-1)
  _qs_partition(A, gt+1, hi)


def quick_sort(A):
  """ Takes an array (list) A and sorts it using Quick-sort. It first randomly shuffles
   the elements in the array. This ensures that the pivot selected in _qs_partition()
   is always randomized.
  """
  random.shuffle(A)   #shuffle the array first
  _qs_partition(A, 0, len(A)-1)
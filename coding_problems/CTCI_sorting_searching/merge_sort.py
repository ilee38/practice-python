#!/usr/bin/env python3

def merge_sort(arr):
  if len(arr) < 2:
    return
  mid = len(arr) // 2
  A = arr[0:mid]
  B = arr[mid:len(arr)]
  merge_sort(A)
  merge_sort(B)
  _merge(arr, A, B)


def _merge(arr, A, B):
  i, j = 0, 0
  for k in range(len(arr)):
    if i > len(A)-1:
      arr[k] = B[j]
      j += 1
    elif j > len(B)-1:
      arr[k] = A[i]
      i += 1
    elif A[i] <= B[j]:
      arr[k] = A[i]
      i += 1
    else:
      arr[k] = B[j]
      j += 1

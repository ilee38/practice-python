#!/usr/local/bin/python3
"""
# Implementation of the Mergesort algorithm
"""

def merge(S, A, B):
  i, j = 0, 0               #keep two aditional indices, one for A and the other for B
  for k in range(len(S)):   #copy the divided arrays A and B back into original S (in sorted order)
    if i > len(A)-1:    #if we reach the end of A, copy whats left on B
      S[k] = B[j]
      j += 1
    elif j > len(B)-1:  #if  we reach the end of B, copy whats left on A
      S[k] = A[i]
      i += 1
    elif B[j] < A[i]:   #copy the smallest element from B
      S[k] = B[j]
      j += 1
    else:               #otherwise copy the smallest from A, and if they're equal
      S[k] = A[i]       #always copy the left array's first to preserve stability
      i += 1


def merge_sort(S):
  if len(S) < 2:      #base case is when only 1 element in list
    return
  mid = len(S) // 2
  A = S[0:mid]          #divide list into two halves
  B = S[mid:len(S)]
  merge_sort(A)         #recursively devide each half
  merge_sort(B)
  merge(S, A, B)      #then merge back (in sorted order)
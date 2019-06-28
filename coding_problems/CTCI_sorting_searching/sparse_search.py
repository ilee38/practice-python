#!/usr/bin/env python3
""" Problem 10.5 from CtCI
"""
def sparse_search(A, s):
	if len(A) == 0 or A is None:
		return None
	#to do: validate arg. s
	return _bin_search(0, len(A)-1, A, s)


def _bin_search(lo, hi, A, s):
	if lo > hi:
		return None
	else:
		mid = (hi + lo) // 2
		if A[mid] == s:
			return mid
		elif A[mid] == '':
			left = _bin_search(lo, mid-1, A, s)
			right = _bin_search(mid+1, hi, A, s)
			if left is None:
				return right
			else:
				return left
		elif A[mid] > s:
			return _bin_search(lo, mid-1, A, s)
		else:
			return _bin_search(mid+1, hi, A, s)
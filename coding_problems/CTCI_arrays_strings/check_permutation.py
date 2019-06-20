#!/usr/bin/env python3

def check_perm(s1, s2):
  if len(s1) != len(s2):
    return False

  A = {}
  for i in range(len(s1)):
    A[s1[i]] = 1 if s1[i] not in A.keys() else A[s1[i]]+1
    A[s2[i]] = 1 if s2[i] not in A.keys() else A[s2[i]]+1

  for j in A.keys():
	  if A[j] % 2 != 0:
		  return False
  return True
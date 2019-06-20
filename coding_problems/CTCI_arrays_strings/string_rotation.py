#!/usr/bin/env python3

""" Problem 1.9 from CtCI book
"""
def str_rotation(s1, s2):
  if len(s1) != len(s2) or len(s1) == 0:
    return False

  s2_char = s2[0]
  for i in range(len(s1)):
    if s2_char == s1[i]:
      if s1[0:i] in s2:   #this would represent the "isSubstring method in the example"
        if len(s1[0:i]) == len(s1)-1:
          return True
        else:
          stop_idx = s2.find(s1[0:i])   #the find() method returns the position of substring s1[0:i]
          k = i
          for j in range(1, stop_idx):
            if s2[j] != s1[k+1]:
              return False
            k += 1
          return True
      else:
        return False
  return False

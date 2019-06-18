#!/usr/bin/env python3
""" Problem 8.7 in CtCI book
"""
def permute(my_str):
  _permute("", my_str)

def _permute(so_far, remaining):
  if len(remaining) == 0:
    print(so_far)
  else:
    for i in range(len(remaining)):
      following = so_far + remaining[i]
      rest = remaining[:i] + remaining[i+1:]
      _permute(following, rest)
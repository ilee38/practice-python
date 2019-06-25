#!/usr/bin/env python3
""" Problem 10.2 from CtCI book
"""

def group_anagrams(A):
  if len(A) == 0 or A is None:
    return None

  word_map = {}
  key = ''
  for word in A:
    key = ''.join(sorted(word))   #the sorted() built-in function returns a list, so
    if key not in word_map:       #it needs to be converted to str in order to be hashable (for the dict)
      word_map[key] = [word]
    else:
      word_map[key].append(word)

  index = 0
  for k in word_map.keys():
    for v in word_map[k]:
      A[index] = v
      index += 1
  return A
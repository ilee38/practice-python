#!/usr/bin/env pyhton3

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
  
def permute(my_str):
  count = 0
  _permute("", my_str, count)


def _permute(so_far, remaining, count):
  if len(remaining) == 0:
    count += 1
    if count == 1000000:
      print(f'count: {count}')
      print(so_far)
    return count 
  else:
    for i in range(len(remaining)):
      following = so_far + remaining[i]
      rest = remaining[:i] + remaining[i+1:]
      count = _permute(following, rest, count)
  return count


def main():
  permute('0123456789')


if __name__ == '__main__':
  main()


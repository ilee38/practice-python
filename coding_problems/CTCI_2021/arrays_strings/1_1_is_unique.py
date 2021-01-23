#!/usr/bin/env python3

""" Solution 1: using additional space
"""
def is_unique(string):
  unique = set()
  for char in string:
    unique.add(char)
  return len(unique) == len(string)


""" Solution 2: no additional space
"""
def is_unique_inplace(string):
  for i in range(len(string)):
    for j in range(i+1, len(string)):
      if string[i] == string[j]:
        return False
  return True


def main():
  print(is_unique('abcdefgh'))
  print(is_unique('abcdeagc'))
  print(is_unique_inplace('abcdefgh'))
  print(is_unique_inplace('abcdeagc'))



if __name__ == "__main__":
  main()
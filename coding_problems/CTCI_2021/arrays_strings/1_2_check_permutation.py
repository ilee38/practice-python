#!/usr/bin/env python3

def is_permutation(string1, string2):
  if len(string1) != len(string2):
    return False
  s1_list = list(string1)
  s2_list = list(string2)
  s1_list.sort()
  s2_list.sort()
  return s1_list == s2_list


def main():
  print(is_permutation('bobcat', 'tacobb'))
  print(is_permutation('bngkl', 'nbl'))
  print(is_permutation('abcdef', 'toperf'))


if __name__ == '__main__':
  main()
#!/usr/bin/env python3
""" Implementation of problem 1.5 - CTCI book
    Check if two strings are one (or zero) edits away
"""
def oneAway(str1, str2):
  if abs(len(str1) - len(str2)) > 1:
    return False
  freqs = {}
  for x in str1:
    if x not in freqs:
      freqs[x] = 1
    else:
      freqs[x] += 1
  for y in str2:
    if y not in freqs:
      freqs[y] = 1
    else:
      freqs[y] += 1
  uniqueCharCount = 0
  for c in freqs:
    if freqs[c] == 1:
      uniqueCharCount += 1
    elif freqs[c] > 2:
      return False
  if len(str1) == len(str2):
    if uniqueCharCount == 2:
      return True
    else:
      return False
  elif uniqueCharCount == 1:
    return True
  else:
    return False


def main():
  print("pale, ple: ", oneAway("pale", "ple"))
  print("pales, pale: ", oneAway("pales", "pale"))
  print("pale, bale: ", oneAway("pale", "bale"))
  print("pale, bake: ", oneAway("pale", "bake"))


if __name__ == '__main__':
  main()
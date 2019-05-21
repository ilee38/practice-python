#!/usr/bin/env python3

""" Problem 1.4 - CTCI
    Define function to check if input string is a permutation of a palindrome
"""
def isPalindromePermutation(inString):
  freq = {}
  string = inString.lower()
  for i in string:
    if i != " ":
      if i not in freq:
        freq[i] = 1
      else:
        freq[i] += 1
  oddCount = 0
  evenCount = 0
  strLen = 0
  for j in freq:
    if freq[j] % 2 == 0:
      evenCount += 1
      strLen += freq[j]
    else:
      oddCount += 1
      strLen += freq[j]
  if strLen % 2 == 0:
    if strLen/evenCount == 2:
      return True
    else:
      return False
  else:
    if oddCount == 1:
      return True
    else:
      return False


if __name__ == '__main__':
  print("Calling function with input string: Tact Coa")
  print("is input string a palindrome permutation? ")
  print(isPalindromePermutation("Tact Coa"))
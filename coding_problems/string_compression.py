#!/usr/bin/env python3
""" Implementation of problem 1.6 from CTCI book
    Method to perfrom basic string compression, based on counts of repeated
    characters
"""
def strCompress(str1):
  count = 1
  prevChar = str1[0]
  compressed = []
  for i in range(1, len(str1)):
    if str1[i] == prevChar:
      count += 1
    else:
      compressed.append(prevChar)
      compressed.append(str(count))
      prevChar = str1[i]
      count = 1
  compressed.append(prevChar)
  compressed.append(str(count))
  if len(str1) > len(compressed):
    return str(compressed)
  else:
    return str1

def main():
  print("aabcccccaaa")
  print("compressed: ", strCompress("aabcccccaaa"))


if __name__ == '__main__':
  main()
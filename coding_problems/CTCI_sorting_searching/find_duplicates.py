#!/usr/bin/env python3
""" Problem 10.8 from CtCI book
"""
def find_dup(Arr):
  dup_bits = bytearray(4000)
  for n in Arr:
    index = n-1		#compensate for 0 indexing
    if not dup_bits[index]:
      dup_bits[index] = 1
    else:
      print(n)

#!/usr/bin/env python3

"""
  The following iterative sequence is defined for the set of positive integers:

  n → n/2 (n is even)
  n → 3n + 1 (n is odd)

  Using the rule above and starting with 13, we generate the following sequence:

  13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

  It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
  Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

  Which starting number, under one million, produces the longest chain?

  Note: Once the chain starts the terms are allowed to go above one million.
"""

def longest_collatz_seq():
  count = 0
  max_count = 0
  starting_n = 0
  for i in range(999999, 2, -1):
    n = i
    while n > 1:
      count += 1
      if n % 2 == 0:
        n = n // 2
      else:
        n = 3*n + 1
    if count > max_count:
      max_count = count
      starting_n = i
    count = 0
  return starting_n


def main():
  print(longest_collatz_seq())


if __name__ == '__main__':
  main()
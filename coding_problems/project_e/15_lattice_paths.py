#!/usr/bin/env python3

""" Starting in the top left corner of a 2×2 grid, and only being able to move to
    the right and down, there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
"""
from math import factorial

def get_num_of_paths(n, k):
  """ Definition (see wikipedia):
      "The number of latttice paths from (0,0) to (n,k) is equal to the binomial
       coefficient (n+k k)"
      the binomial coefficient is the combination nCk. In this case n = n+k.
  """
  num_paths = factorial(n+k) // (factorial(k) * factorial(k))
  return num_paths


def main():
  print('Number of lattice paths in a 20x20 grid:')
  print(get_num_of_paths(20,20))


if __name__ == "__main__":
  main()
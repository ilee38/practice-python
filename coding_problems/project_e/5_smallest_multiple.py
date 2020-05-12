#!/usr/bin/env python3

""" 2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
"""
def smallest_multiple():
  divisors = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  divisible = True
  multiple = 20
  while True:
    for i in range(len(divisors)):
      if multiple % divisors[i] != 0:
        divisible = False
        break
    if divisible:
      return multiple
    multiple += 20
    divisible = True

def main():
  print(smallest_multiple())

if __name__ == '__main__':
  main()
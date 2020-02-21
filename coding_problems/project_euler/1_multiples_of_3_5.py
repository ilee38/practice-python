#!/usr/bin/env python3
""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_multiples(num1, num2, limit):
  multiple = 0
  multiples = set()
  for i in range(1, limit):
    multiple = num1 * i
    if multiple < limit:
      multiples.add(multiple)
    elif multiple >= limit:
      break
  for j in range(1, limit):
    multiple = num2 * j
    if multiple < limit:
      multiples.add(multiple)
    elif multiple >= limit:
      break
  return sum(multiples)

def main():
  total = find_multiples(3, 5, 1000)
  print("the sum is: ", total)

if __name__ == "__main__":
  main()



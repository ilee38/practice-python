#!/usr/bin/env python3
"""
  n! means n × (n − 1) × ... × 3 × 2 × 1

  For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
  and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

  Find the sum of the digits in the number 100!
"""

from math import factorial

def factorial_digit_sum(digit):
  fact = factorial(digit)
  str_fact = str(fact)
  digit_sum = 0
  for n in str_fact:
    digit_sum += int(n)
  return digit_sum


def rec_factorial(n):
  if n == 1:
    return 1
  return n * rec_factorial(n-1)


def main():
  print(factorial_digit_sum(100))


if __name__ == '__main__':
  main()
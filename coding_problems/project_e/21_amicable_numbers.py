#!/usr/bin/env python3
""" Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
  If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

  Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
  """ Returns the sum of proper divisors of n
  """
  divisors = []
  for i in range(1, n):
    if n % i == 0:
      divisors.append(i)
  return sum(divisors)


def amicable_nums(N):
  amicables = set()
  for a in range(N):
    b = d(a)
    test = d(b)
    if test == a and a != b:
      amicables.add(a)
      amicables.add(b)
  return sum(amicables)


def main():
  print(amicable_nums(10000))


if __name__ == '__main__':
  main()
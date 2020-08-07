#!/usr/bin/env python3

""" A perfect number is a number for which the sum of its proper divisors is exactly equal to the
number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all
integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def proper_div_sum(n):
  """ Returns the sum of the proper divisors of n
  """
  total = 0
  for i in range(1, n):
    if n % i == 0:
      total += i
  return total


def find_abundant_nums(limit):
  """ Returns the set of abundant numbers up to arg: limit (not inclusive)
  """
  abundants = []
  for n in range(1, limit):
    divisors_sum = proper_div_sum(n)
    if divisors_sum > n:
      abundants.append(n)
  return abundants


def non_abundant_sum(sum_of_abundants):
  """ Returns the sum of numbers that are not the sum of two abundant numbers.
  """
  total = 0
  for n in range(1, 28123):
    if n not in sum_of_abundants:
      total += n
  return total


def nums_equal_to_abundants_sum(abundants):
  """ Returns the set of numbers that are equal to the sum of two abundant
      numbers
  """
  sums_of_abundants = set()
  for i in range(len(abundants)):
    for j in range(len(abundants)):
      if abundants[i] + abundants[j] < 28123:
        sums_of_abundants.add(abundants[i] + abundants[j])
      else:
        break
  return sums_of_abundants


def main():
  abundant = find_abundant_nums(28123)
  abundant_sums = nums_equal_to_abundants_sum(abundant)
  print('Non-abundants sum', non_abundant_sum(abundant_sums))


if __name__ == '__main__':
  main()
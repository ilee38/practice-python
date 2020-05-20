#!/usr/bin/env python3

""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""


def get_primes(s):
  """ Generates primes using the Sieve of Eratosthenes
      Includes the optimization where for every prime p, only factors p >= p^2
      are verified.
      The list of primes is represented with a bytearray. Each index corresponds
      to an integer in the list. A value of "1" at the index location indicates
      the integer is a prime.
  """
  primes = bytearray([1]*s)
  for i in range(2, s):
      if primes[i] == 1:
        for j in range(i, s):
          if i*j < s:
            primes[i*j] = 0
          else:
            break
  return primes


def main():
  primes = get_primes(2000000)
  summation = 0
  for i in range(2, len(primes)):
    if primes[i] == 1:
      summation += i
  print(summation)


if __name__ == '__main__':
  main()
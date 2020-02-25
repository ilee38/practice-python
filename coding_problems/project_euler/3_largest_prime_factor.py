#!/usr/bin/env python3

""" The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600,851,475,143 ?
"""
from math import sqrt

def largest_prime_factor(num):
  length = int(sqrt(num)) + 1
  primes = bytearray(length)
  get_primes(primes)
  for i in range(length-1, -1, -1):
    if primes[i] == 0:
      if num % i == 0:
       return i

def get_primes(primes):
  """ Use the Sieve of Erathostenes to generate prime numbers up to
      n = sqrt(num) = len(primes)
  """
  for i in range(2, len(primes)):
    if primes[i] == 0:
      for j in range(2, len(primes)):
        if i*j < len(primes):
          primes[i*j] = 1
        else:
          break

def main():
  print("largest prime factor:", largest_prime_factor(600851475143))

if __name__ == "__main__":
  main()
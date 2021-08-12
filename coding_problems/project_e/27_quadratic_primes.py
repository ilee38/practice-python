#!/usr/bin/env python3

"""
Euler discovered the remarkable quadratic formula:
n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer
values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
by 41.
The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80
primes for the consecutive values $0 \le n \le 79$. The product of the coefficients,
 −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000 where |n| is the modulus/absolute
value of n e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.
"""

def primes_list(length):
   primes = [2]
   for i in range(3, length, 2):
      for j in range(2, int(i ** 0.5) + 1):
         if i % j == 0:
               break
      else:
         primes.append(i)
   return primes


def quadratic_primes(a, b, primes):
   consecutive_primes = 0

   for n in range(len(primes)):
      value = n**2 + a*n + b
      if value in primes:
         consecutive_primes += 1
      else:
         break
   return consecutive_primes


def main():
   max_consecutive_primes = 0
   primes = primes_list(2000)
   best_a = 0
   best_b = 0
   for b in range(1001):
      for a in range(-999, 1000):
         primes_count = quadratic_primes(a, b, primes)
         if primes_count > max_consecutive_primes:
            max_consecutive_primes = primes_count
            best_a = a
            best_b = b
   print (f'Max consecutive primes: {max_consecutive_primes}')
   print(f'a: {best_a} b: {best_b}')
   print(f'a*b: {best_a*best_b}')


if __name__ == "__main__":
   main()
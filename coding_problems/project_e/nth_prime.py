#!/usr/bin/env python3

""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?
"""


def nth_prime(nth):
  """ Find the nth prime by trial and error, using the Sieve of Eratosthenes
      with an increasingly large size of n (where n is the limit). I.e. the
      Sieve of Eratosthenes finds all prime numbers up to a given limit n.

      Start with n = (nth * 2) and count how many primes are found. If
      less than "nth" then increase n by a factor of 1 and start again:
          - use a bytearray initialized with 1's
          - set each non-prime to 0 (during the sieve of eratosthenes)
          - after finishing running the sieve of eratosthenes:
              just sum up the bytearray to find the total number of primes
  """
  num_primes = 0
  trial_num = 2
  while num_primes < nth:
    n = (nth * trial_num)
    primes = bytearray([1]*n)   #bytearray initialized with 1's
    for i in range(2, n):
      if primes[i] == 1:
        for j in range(2, n):
          if i*j < n:
            primes[i*j] = 0
          else:
            break
    num_primes = sum(primes[2:])
    trial_num += 1

  count = 0
  for k in range(2, n):       #find the 10,001st prime by finding the index of the
    count += primes[k]        #10,001st "1"
    if count == nth:
      return (k, num_primes)


def main():
    nth = 10001
    my_prime, total_primes = nth_prime(nth)
    print("Found {} prime numbers. The nth = {} prime is: {}".format(total_primes, nth, my_prime))


if __name__ == "__main__":
    main()
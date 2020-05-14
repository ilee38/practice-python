#!/usr/bin/env python3

""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?
"""


def ten_thousand_1st_prime():
  """ Find the 10,0001st prime by trial and error, using the Sieve of Eratosthenes
      with an increasingly large size of n (where n is the limit). I.e. the
      Sieve of Eratosthenes finds all prime numbers up to a given limit n.

      Start with n = (10,0001 * 2) and count how many primes are found. If
      less than 10,0001 then double n and start again:
          - use a bytearray initialized with 1's
          - set each non-prime to 0 (during the sieve of eratosthenes)
          - after finishing running the sieve of eratosthenes:
              just sum up the bytearray to find the total number of primes
  """
  n = (10001 * 11)            #after trial and error, (10001*11) gives 10,453 primes
  primes = bytearray([1]*n)   #bytearray initialized with 1's
  for i in range(2, n):
    if primes[i] == 1:
      for j in range(2, n):
        if i*j < n:
          primes[i*j] = 0
        else:
          break
  num_primes = sum(primes[2:])
  count = 6                   #13 is the 6th prime, so start count at 6 and from index 14
  for k in range(14, n):      #find the 10,001st prime by finding the index of the
    count += primes[k]        #10,001st "1"
    if count == 10001:
      return (k, num_primes)


def main():
    my_prime, total_primes = ten_thousand_1st_prime()
    print("Found {} prime numbers. The 10,001st prime is {}".format(total_primes, my_prime))


if __name__ == "__main__":
    main()
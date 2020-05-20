#!/usr/bin/env python3

""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
      a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

def product():
  """ Uses Euclid's formula to generate pythagorean triples.
      Given an arbitrary pair of integers m and n with m > n > 0,
      the formula states that the integers
              a = m^2 - n^2, b = 2mn, c = m^2 + n^2
      form a Pythagorean triple.
  """
  a = 0
  b = 0
  c = 0
  for n in range(1, 1001):
    for m in range(n+1, 1001):
      a = (m**2)-(n**2)
      b = 2*m*n
      c = (m**2)+(n**2)
      if a+b+c == 1000:
        return (a*b*c)


def main():
  print('Product: {}'.format(product()))


if __name__ == '__main__':
  main()
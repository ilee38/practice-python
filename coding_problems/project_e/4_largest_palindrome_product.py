#!/usr/bin/env python3

""" A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def get_largest_pal():
  largest = 0
  for i in range(999, 99, -1):
    for j in range(999, 99, -1):
      product = i*j
      if is_palindrome(product):
        if product > largest:
          largest = product
  return largest


def is_palindrome(num):
  num_str = str(num)
  ptr1 = 0
  ptr2 = len(num_str)-1
  while ptr1 < ptr2:
    if num_str[ptr1] != num_str[ptr2]:
      return False
    ptr1 += 1
    ptr2 -= 1
  return True


def main():
  print(get_largest_pal())


if __name__ == "__main__":
  main()
#!/usr/bin/env python3
"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.
"""
def even_fib_sum(limit):
  table = {1: 1, 2: 2}
  sum = 2
  n = 3
  while True:
    table[n] = table[n-1] + table[n-2]
    next = table[n]
    if next > limit:
      break
    if next % 2 == 0:
      sum += next
    n += 1
  return sum

def main():
  sum = even_fib_sum(4000000)
  print("sum is: ", sum)

if __name__ == "__main__":
  main()


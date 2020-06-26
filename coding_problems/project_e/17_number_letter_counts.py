#!/usr/bin/env python3
"""
  If the numbers 1 to 5 are written out in words: one, two, three, four, five,
  then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

  If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
  words, how many letters would be used?


  Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
        contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
        The use of "and" when writing out numbers is in compliance with British usage.
"""

def count_letters():
  one_fig = ['one','two','three','four','five','six','seven','eight','nine']
  teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen', 'nineteen']
  two_fig = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
  total_letters = 0

  #Count 1 thru 19
  for i in one_fig:
    total_letters += len(i)
  for j in teens:
    total_letters += len(j)

  #Count 20 thru 99
  for k in two_fig:
    total_letters += len(k)
    for l in one_fig:
      total_letters += len(k) + len(l)

  #Count 100 thru 999
  len_hundred = len('hundred')
  len_and = len('and')
  for m in one_fig:
    total_letters += len(m) + len_hundred
    for n in one_fig:
      total_letters += len(m) + len_hundred + len_and + len(n)
    for o in teens:
      total_letters += len(m) + len_hundred + len_and + len(o)
    for p in two_fig:
      total_letters += len(m) + len_hundred + len_and + len(p)
      for q in one_fig:
        total_letters += len(m) + len_hundred + len_and + len(p) + len(q)

  #Count 1000
  total_letters += len('one') + len('thousand')
  return total_letters


def main():
  print(count_letters())


if __name__ == '__main__':
  main()

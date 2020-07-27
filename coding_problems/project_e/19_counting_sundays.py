#!/usr/bin/env python3
"""
  You are given the following information, but you may prefer to do some research for yourself.

  - 1 Jan 1900 was a Monday.
  - Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
  - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

  How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from calendar import Calendar

def sundays_on_first():
  count = 0
  cal = Calendar()
  for year in range(1901, 2001):
    for month in range(1, 13):
      it = cal.itermonthdays2(year, month)
      for month_day in it:
        if month_day[0] == 1 and month_day[1] == 6:
          count += 1
  return count


def main():
  print(sundays_on_first())


if __name__ == '__main__':
  main()
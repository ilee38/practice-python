#!/usr/bin/env python3

def pow_digit_sum(power):
  total_sum = 0
  str_qty = str(2**power)
  for digit in str_qty:
    total_sum += int(digit)
  return total_sum


def main():
  print(pow_digit_sum(1000))


if __name__ == '__main__':
  main()
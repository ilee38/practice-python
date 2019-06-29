#!/usr/bin/env python3
""" Problem 16.8 from CtCI book
"""
def english_int(num):
  if num == 0:
    return 'zero'

  lookup = {'0': ['', '',''],
            '1': ['one', 'ten', 'one hundred'],
            '2': ['two', 'twenty', 'two hundred'],
            '3': ['three', 'thirty', 'three hundred'],
            '4': ['four', 'forty', 'four hundred'],
            '5': ['five', 'fifty', 'five hundred'],
            '6': ['six', 'sixty', 'six hundred'],
            '7': ['seven', 'seventy', 'seven hundred'],
            '8': ['eight', 'eighty', 'eight hundred'],
            '9': ['nine', 'ninety', 'nine hundred']
            }
  final = []
  str_num = str(num)
  if num < 0:
    str_num = str_num[1:]

  if len(str_num) <= 3:
    final.append(process_chunk(str_num, lookup))
  else:
    div_times = len(str_num) // 3
    remainder = len(str_num) % 3
    if remainder > 0:
      final.append(process_chunk(str_num[:remainder], lookup))
    for i in range(div_times):
      final.append(process_chunk(str_num[remainder:remainder+3], lookup))
      remainder += 3
  if num < 0:
    print('negative ' + print_num(final))
  else:
    print(print_num(final))


def process_chunk(str_num, lookup):
  teens = ('', 'eleven', 'twleve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
  length = len(str_num)
  result = ''
  for i in range(length):
    if len(str_num[0:length-i]) == 2:
      if int(str_num[i]) == 1 and int(str_num[i+1]) > 0 and int(str_num[i+1]) <= 9:
        result += teens[int(str_num[i+1])]
        return result
      else:
        result += lookup[str_num[i]][(length-1)-i]+' '
    else:
      result += lookup[str_num[i]][(length-1)-i]+' '
  return result


def print_num(final):
  magnitude = ('','','thousand', 'million(s)', 'billion(s)')
  eng_int = ''
  for i in range(len(final)):
    eng_int += final[i]+' '+magnitude[len(final)-i]+' '
  return eng_int




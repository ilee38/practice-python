#!/usr/bin/env python3

def urlify(string_array, size):
  num_inserts = 0
  # count number of spaces
  for i in range(size):
    if string_array[i] == ' ':
      num_inserts += 1
  # we need 2 extra spaces per insertion of '%20'
  shift = num_inserts * 2
  # move characters starting from the end
  for j in range(size-1, -1, -1):
    if string_array[j] != ' ':
      string_array[j + shift] = string_array[j]
    else:
      string_array[j + shift] = '0'
      string_array[j + (shift-1)] = '2'
      string_array[j + (shift-2)] = '%'
      # since we filled 2 of the extra spaces, we decrease the amount of shift
      shift -= 2
  return string_array


def main():
  string = 'Mr John Smith'
  size = len(string)
  string_array = [''] * (2*size)
  for i in range(len(string)):
    string_array[i] = string[i]
  print(string_array)
  arr = urlify(string_array, size)
  for k in range(len(arr)):
    print(arr[k], end='')
  print('\n')

if __name__ == '__main__':
  main()

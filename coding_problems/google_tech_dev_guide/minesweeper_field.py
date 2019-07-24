#!/usr/bin/env python3
"""
  Problem: implement functions to construct the playing field
  of minesweeper given the size and number of mines
"""
from random import randint

def construct_field(m, n, num_mines):
  if num_mines > m*n:
    raise ValueError('Number of mines is greater than available cells')

  if num_mines <= (m*n)/2:
    field = fillup('empty', m, n)
    mines_left = num_mines
    while(mines_left > 0):
      x = randint(0, m-1)
      y = randint(0, n-1)
      if field[x][y] != 1:
        field[x][y] = 1
        mines_left -= 1
  else:
    field = fillup('full', m, n)
    space_left = (m*n) - num_mines
    while(space_left > 0):
      x = randint(0, m-1)
      y = randint(0, n-1)
      if field[x][y] != 0:
        field[x][y] = 0
        space_left -= 1
  #Todo: update mine counts for adjacent mines
  return field


def fillup(element, m, n):
  if element == 'empty':
    field = [[0] * m for i in range(n)]
    return field
  elif element == 'full':
    field = [[1] * m for i in range(n)]
    return field
  else:
    raise ValueError('element argument is invalid')


def main():
  field_1 = construct_field(10, 10, 35)
  field_2 = construct_field(10, 10, 90)
  for i in range(10):
    print(field_1[i])
  print('==============================')
  for i in range(10):
    print(field_2[i])

if __name__ == '__main__':
  main()
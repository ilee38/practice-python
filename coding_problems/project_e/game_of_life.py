#!/usr/bin/env python3

""" Conway's Game of Life
"""
import copy

def game_of_life(grid_size, ticks):
  curr_grid = [[0]*grid_size for _ in range(grid_size)]
  next_grid = [[0]*grid_size for _ in range(grid_size)]
  init_setup(curr_grid)
  for tick in range(ticks):
    next_grid = next_state(curr_grid, next_grid)
    curr_grid = copy.deepcopy(next_grid)
    print_grid(curr_grid)


def next_state(curr_grid, next_grid):
  size = len(curr_grid)
  alive = False
  field_sum = 0
  for r in range(size):
      for c in range(size):
        if r > 0:
          field_sum += sum(curr_grid[r-1][c-1:c+2])
        field_sum += sum(curr_grid[r][c-1:c+2])
        if r < size-1:
          field_sum += sum(curr_grid[r+1][c-1:c+2])
        if curr_grid[r][c] == 1:
          alive = True
          field_sum -= 1  #count neighbors only
        if alive and (field_sum > 1 and field_sum <= 3):
          next_grid[r][c] = 1
        elif not alive and field_sum == 3:
          next_grid[r][c] = 1
        else:
          next_grid[r][c] = 0
        field_sum = 0
        alive = False
  return next_grid


def init_setup(curr_grid):
  """Creates the initial state of the grid
  """
  #set up a "blinker"
  # curr_grid[4][3] = 1
  # curr_grid[4][4] = 1
  # curr_grid[4][5] = 1

  #set up a "toad"
  # curr_grid[3][4] = 1
  # curr_grid[3][5] = 1
  # curr_grid[3][6] = 1
  # curr_grid[4][3] = 1
  # curr_grid[4][4] = 1
  # curr_grid[4][5] = 1

  #set up a "glider"
  curr_grid[1][3] = 1
  curr_grid[2][1] = 1
  curr_grid[2][3] = 1
  curr_grid[3][2] = 1
  curr_grid[3][3] = 1

  print_grid(curr_grid)


def print_grid(grid):
  print("")
  for i in range(len(grid)):
    print(grid[i])
  print("")


def main():
  game_of_life(10, 8)


if __name__ == '__main__':
  main()
#!/usr/bin/env python3

""" Conway's Game of Life
"""
import copy

def game_of_life(grid_size, periods):
  curr_grid = [[0]*grid_size for _ in range(grid_size)]
  next_grid = [[0]*grid_size for _ in range(grid_size)]
  init_setup(curr_grid)
  for tick in range(periods):
    next_grid = next_state(curr_grid, next_grid)
    curr_grid = copy.deepcopy(next_grid)
    print("Period: {}".format(tick+1))
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
  #set up a "glider"
  curr_grid[1][3] = 1
  curr_grid[2][1] = 1
  curr_grid[2][3] = 1
  curr_grid[3][2] = 1
  curr_grid[3][3] = 1
  print_grid(curr_grid)   #print the initial state


def print_grid(grid):
  for i in range(len(grid)):
    print(grid[i])
  print("\n")


def main():
  """ Start Game of Life with a 10x10 grid, and run it for 20 periods
  """
  game_of_life(10, 20)


if __name__ == '__main__':
  main()
#!/usr/bin/env python3

""" Problem 8.2 in CtCI book
"""
def getPath(maze):
  """ args: maze is a [r]x[c] matrix
  """
  if len(maze) == 0 or maze is None:
    return None
  failedPoints = set()
  path = []
  if _getPath(maze, len(maze), len(maze[0]), path, failedPoints):
    return path
  return None

def _getPath(maze, row, col, path, failedPoints):
  if row < 0 or col < 0:
    return False
  if (row, col) in failedPoints:
    return False
  at_origin = row==0 and col==0
  if at_origin or _getPath(maze, row-1, col, path, failedPoints) or\
  _getPath(maze, row, col-1, path, failedPoints):
    path.append((row,col))
    return True
  else:
    failedPoints.add((row,col))
    return False


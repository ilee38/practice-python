#!/usr/bin/env python3

""" Problem 1.8 from CTCI book
    Zero Matrix
"""

def zeroMatrix(M):
  rows = set()
  cols = set()
  for i in range(len(M)):
    for j in range(len(M)):
      if M[i][j] == 0:
        rows.add(i)
        cols.add(j)
  for r in rows:
    for k in range(len(M)):
      M[r][k] = 0
  for c in cols:
    for l in range(len(M)):
      M[l][c] = 0
  return M


def main():
  M = [[3,0,45,6],[9,87,0,38],[46,32,91,21],[25,9,71,51]]
  for row in M:
    print(row)
  print('------')
  M = zeroMatrix(M)
  for row in M:
    print(row)


if __name__ == '__main__':
  main()
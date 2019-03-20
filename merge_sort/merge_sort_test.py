"""
# Test file for Mergesort algorithm implementation
"""

from merge_sort import merge_sort

if __name__ == '__main__':
  S = [325432, 989,   547510, 3,   -93,  189019, 5042,  123,
                    597,    42,    7506,   184, 184,  2409,   45,    824,
                    4,      -2650, 9,      662, 3928, -170,   45358, 395,
                    842,    7697,  110,    14,  99,   221]

  print("Unsorted array:")
  print(str(S))

  merge_sort(S)
  print("Sorted array:")
  print(str(S))
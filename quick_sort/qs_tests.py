"""
# Tests for the quick-sort implementation
"""
from quick_sort import quick_sort

if __name__ == '__main__':
  A = [325432, 989,   547510, 3,   -93,  189019, 5042,  123,
                    597,    42,    7506,   184, 184,  2409,   45,    824,
                    4,      -2650, 9,      662, 3928, -170,   45358, 395,
                    842,    7697,  110,    14,  99,   221]
  print("Initial unsorted array:")
  print(str(A))
  print("Sorting array with quick-sort")
  quick_sort(A)
  print("Sorted array:")
  print(str(A))
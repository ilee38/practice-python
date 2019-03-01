"""
# Implementation of a recursive binary search algorithm
# Returns the index of the target element in a sorted array
"""
def binarySearch(arr, target, low, high):
  mid = (low + high) // 2
  if arr[mid] == target:
    return mid
  elif low > high:
    return -1
  if arr[mid] > target:
    return binarySearch(arr, target, low, mid-1)
  else:
    return binarySearch(arr, target, mid+1, high)


# Tests for the binarySearch function
if __name__ == '__main__':
  myArr = [5, 6]
  indexOfTarget = binarySearch(myArr, 5, 0, len(myArr)-1)
  print("index of 5: ", indexOfTarget)
  indexOfTarget = binarySearch(myArr, 6, 0, len(myArr)-1)
  print("index of 6: ", indexOfTarget)
  myArr2 = [1, 8, 11, 51, 78, 95, 132, 256, 389]
  targetIndex = binarySearch(myArr2, 132, 0, len(myArr2)-1)
  print("index of 132: ", targetIndex)
  targetIndex = binarySearch(myArr2, 1, 0, len(myArr2)-1)
  print("index of 1: ", targetIndex)
  targetIndex = binarySearch(myArr2, 389, 0, len(myArr2)-1)
  print("index of 389: ", targetIndex)




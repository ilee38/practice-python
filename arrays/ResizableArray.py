#!/usr/local/bin/python3

import ctypes

# Implements an automatically resizable array
class ResizableArray():
  def __init__(self, cap=1):
    self._items = 0
    self._capacity = cap
    self._A = self._make_array(self._capacity)

  # Return number of items in the array
  def size(self):
    return self._items

  # Returns the array's current capacity
  def get_capacity(self):
    return self._capacity

  # Returns boolean value
  def is_empty(self):
    if self._items == 0:
      return True
    return False

  # Returns item at given index, or error if incorrect index
  def at(self, index):
    if index > self._items or index < 0:
      raise IndexError("invalid index")
    return self._A[index]

  # Inserts an item at the end of the array. Grows the array if capacity is full
  def push(self, element):
    if self._items == self._capacity:
      self._resize(2 * self._capacity)  #double the capacity
    self._A[self._items] = element
    self._items += 1  #update items count

  # Resizes the array to new capacity
  def _resize(self, cap):
    B = self._make_array(cap)
    for i in range(self._items):
      B[i] = self._A[i]
    self._A = B
    self._capacity = cap  #update capacity count

  # Creates a new array using the ctypes module
  def _make_array(self, cap):
    return (cap * ctypes.py_object)()


### TEST SECTION ###
if __name__ == '__main__':
  myArray = ResizableArray()
  print("* array's capacity: ", myArray.get_capacity())
  print("* items in my array (size): ", myArray.size())
  print("* is the array empty? ", myArray.is_empty())
  print("* push 9 into array...")
  myArray.push(9)
  print("* is the array empty? ", myArray.is_empty())
  print("* value at index 0: ", myArray.at(0))
  print("* push 21 into array...")
  myArray.push(21)
  print("* new size: ", myArray.size())
  print("* new capacity: ", myArray.get_capacity())
  #print("* request out-of-bounds index...")
  #myArray.at(10)
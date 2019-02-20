#!/usr/local/bin/python3

"""
# Implementation of a Queue using a fixed-size array
"""
import ctypes       #library to create raw arrays

class ArrayQueue:

  ARRAY_SIZE = 100    #default fixed array's size

  def __init__(self):
    self._data = self._make_array(ArrayQueue.ARRAY_SIZE)
    self._size = 0


  def enqueue(self, val):
    if self._size >= ArrayQueue.ARRAY_SIZE - 1:
      raise IndexError("Queue is full")
    self._data[self._size] = val          #add value at the end of the array
    self._size += 1


  def dequeue(self):
    if self._size == 0:
      raise IndexError("Queue is empty")
    ret_val = self._data[0]              #return value from the front of the array
    for i in range(1, self._size):       #move elements up the queue by 1 position
      self._data[i-1] = self._data[i]
    self._data[self._size] = None        #after the loop, the last index remains the same, so set it to None afterward
    self._size -= 1
    return ret_val


  def empty(self):
    return self._size == 0


  def _make_array(self, size):
    return (size * ctypes.py_object)()    #create raw array w/ctypes library
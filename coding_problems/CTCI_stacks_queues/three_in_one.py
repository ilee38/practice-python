#!/usr/bin/env python3
""" Problem 3.1 from the CtCI book
"""

class ThreeInOne:
  """ Assume the stack sizes are fixed. The total size of the array is given.
  """
  def __init__(self, size):
    self._size = size
    self._arr = [None]*size
    self._max_size = size // 3    #max size of ea. stack
    self._st1_curr_size = 0
    self._st2_curr_size = 0
    self._st3_curr_size = 0


  def push(self, st_num, val):
    """
      args:
        st_num = stack number (1, 2 or 3)
        val = value to push
    """
    st_ptr, st_sz = self._st_info(st_num)
    if st_sz == self._max_size:
      raise ValueError('stack: ', st_num, ' is full')
    else:
      self._arr[st_ptr+1] = val
      self._update_sz(st_num, 1)   #increase stack size


  def pop(self, st_num):
    """
      args:
        st_num = stack number (1, 2 or 3)
    """
    st_ptr, st_sz = self._st_info(st_num)
    if st_sz == 0:
      raise ValueError('stack: ', st_num, ' is empty')
    else:
      e = self._arr[st_ptr]
      self._remove_elem(st_ptr, st_num)
      return e


  def _st_info(self, st_num):
    """
      Returns a tuple representing (stack pointer, current size of given stack number)
      returns tuple:
        - stack pointer = index of top element in the stack
        - current size (num of elements) of the stack
    """
    if st_num == 1:
      return (self._st1_curr_size-1, self._st1_curr_size)
    elif st_num == 2:
      return ((self._size//3)+(self._st2_curr_size-1), self._st2_curr_size)
    elif st_num == 3:
      return (2*(self._size//3)+(self._st3_curr_size-1), self._st3_curr_size)
    else:
      raise ValueError('Invalid stack number')


  def _update_sz(self, st_num, delta):
    """
      Updates the current size of the given stack number.
      args:
        st_num = stack number
        delta: if == 1 increase size, if == -1 decrease size
    """
    if st_num == 1:
      self._st1_curr_size += delta
    elif st_num == 2:
      self._st2_curr_size += delta
    elif st_num == 3:
      self._st3_curr_size += delta
    else:
      raise ValueError('Invalid stack number')


  def _remove_elem(self, st_ptr, st_num):
    """
      Removes element from stack (i.e. sets it to None and decreases stack size)
    """
    self._arr[st_ptr] = None
    self._update_sz(st_num, -1)   #decrease stack size
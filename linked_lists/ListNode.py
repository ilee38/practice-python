#!/usr/local/bin/python3

"""
# Class definition of a list node
"""

class ListNode:

  #Constructor with default values
  def __init__(self, val=0, nxt=None):
    self._value = val
    self._next = nxt

  def get_value(self):
    return self._value

  def get_next(self):
    return self._next

  def set_value(self, v):
    self._value = v

  def set_next(self, n):
    self._next = n
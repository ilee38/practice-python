#!/usr/local/bin/python3

"""
# Implementation of HashItem class, which represents an element in a hash table
"""
class HashItem:
  __slots__ = '_key', '_value'

  def __init__(self, k, v):
    self._key = k
    self._value = v


  def get_key(self):
    return self._key


  def get_value(self):
    return self._value


  def set_key(self, k):
    self._key = k


  def set_value(self, v):
    self._value = v
#!/usr/bin/env python3
""" Problem 3.4 from CtCI book
"""
from collections import deque

class MyQueue:
  def __init__(self):
    self._st1 = deque()
    self._st2 = deque()

  def enqueue(self, val):
    self._st1.append(val)

  def dequeue(self):
    if len(self._st1) == 0 and len(self._st2) == 0:
      raise ValueError('Queue is empty')
    if len(self._st2) > 0:
      elem = self._st2.pop()
      return elem
    else:
      for i in range(len(self._st1)):
        self._st2.append(self._st1.pop())
      elem = self._st2.pop()
      return elem

  def peek(self):
    if len(self._st1) == 0 and len(self._st2) == 0:
      raise ValueError('Queue is empty')
    if len(self._st2) > 0:
      elem = self._st2.pop()
      self._st2.append(elem) 	#replace elem into st2
      return elem
    else:
      for i in range(len(self._st1)):
        self._st2.append(self._st1.pop())
      elem = self._st2.pop()
      self._st2.append(elem)	#replace elem into st2
      return elem
#!/usr/bin/env python3

""" Problem 3.3 on CtCI book
"""
class StackSet:
  THR = 5     #threshold for stack size

  class Node:
    def __init__(self, val):
      self.val = val
      self.next = None

  def __init__(self, val=None):
    new_elem = self.Node(val)
    self._head = new_elem
    self._N = 1     #total num of elements
    self._S = 1     #num of stacks in set
    self._h_tbl = {self._S: self._head}

  def push(self, val):
    elem = self.Node(val)
    if self._N % self.THR == 0:
      self._h_tbl[self._S + 1] = elem
      self._S += 1
    elem.next = self._head
    self._head = elem
    self._N += 1

  def pop(self):
    if self._head is None:
      raise ValueError("Stack is empty")
    print(self._head.val)
    self._head = self._head.next
    if(self._N - 1) % self.THR == 0:
      self._S -= 1
    self._N -= 1
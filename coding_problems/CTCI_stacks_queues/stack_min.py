#!/usr/bin/env python3

""" Problem 3.2 on CtCI book
"""
class Stack:

  class Node:
    def __init__(self, val):
      self.val = val
      self.next = None


  def __init__(self, value=None):
    new_node = self.Node(value)
    self._head = new_node
    self._size = (1 if value is not None else 0)

  def push(self, val):
    #todo: validate val argument
    new_node = self.Node(val)
    self.update_head(self, new_node)
    self._size += 1

  def pop(self):
    self.remove_head(self)

  def update_head(self, stack, node):
    """ Make arg: node the new head
    """
    node.next = stack._head
    stack._head = node

  def remove_head(self, stack):
    stack._head = stack._head.next


class StackWithMin(Stack):
  """ Stack class with min() method running in O(1)
  """
  def __init__(self, val):
    self._mins_stack = Stack(val)

  def push(self, val):
    if val < self._mins_stack._head.val:
      new_node = self.Node(val)
      self.update_head(self._mins_stack, new_node)
    super().push(val)
    self._size += 1


  def pop(self):
    if self._head.val == self._mins_stack._head.val:
      self.remove_head(self._mins_stack)
    super().pop()

  def min(self):
    return self._mins_stack._head.val





#!/usr/local/bin/python3
"""
# Implementation of BinarySearchTree class
"""
class BinarySearchTree:

  ##
  # Nested class representing a tree node
  # the __slots__ declaration is used to streamline memory usage
  ##
  class Node:
    __slots__ = '_data', '_left', '_right'
    def __init__(self, data):
      self._data = data
      self._left = None
      self._right = None


  def __init__(self):
    self._root = None


  def insert(self, node, value):
    if node == None:
      node = Node(value)
      return node
    if value < node._data:
      node._left = self.insert(node._left, value)
    elif value > node._data:
      node._right = self.insert(node._right, value)
    return node


  ##
  # Prints sorted values, with DFS in-order traversal
  #
  def printValues(self, root):
    if root == None:
      return
    self.printValues(root._left)
    print(root._data, " ")
    self.printValues(root._right)


  def deleteTree(self, root):

  def isInTree(self, node, value):

  def getHeight(self, root):

  def getMin(self, root):

  def getMax(self, root):

  def isBinarySearchTree(self, root):

  def deleteValue(self, node, value):

  def getSuccessor(self, root, value):

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

  def insert(self, value):

  def printValues(self, root):

  def deleteTree(self, root):

  def isInTree(self, node, value):

  def getHeight(self, root):

  def getMin(self, root):

  def getMax(self, root):

  def isBinarySearchTree(self, root):

  def deleteValue(self, node, value):

  def getSuccessor(self, root, value):

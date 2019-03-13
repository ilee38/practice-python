#!/usr/local/bin/python3
"""
# Implementation of BinarySearchTree class
"""
from collections import deque

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
      node = self.Node(value)
      return node
    if value < node._data:
      node._left = self.insert(node._left, value)
    elif value > node._data:
      node._right = self.insert(node._right, value)
    return node


  def printValues(self, root):
    """
    Prints sorted values, with DFS in-order traversal
    """
    if root == None:
      return
    self.printValues(root._left)
    print(root._data, " ")
    self.printValues(root._right)


  def deleteTree(self, root):
    if root == None:
      return
    if root._left != None:
      self.deleteTree(root._left)
    elif root._right != None:
      self.deleteTree(root._right)
    root = None


  def isInTree(self, node, value):
    if node == None:
      return False
    if value == node._data:
      return True
    if value < node._data:
      return self.isInTree(node._left, value)
    elif value > node._data:
      return self.isInTree(node._right, value)


  def getHeight(self, node):
    """
    Returns the height of a node, defined as the number of edges on the longest
    path from the specified node to a leaf node. Single node height is 1.
    """
    if node == None:
      return -1       #return -1 because we're counting edges, not nodes.
    heightLeftTree = self.getHeight(node._left)
    heightRightTree = self.getHeight(node._right)
    return max(heightLeftTree, heightRightTree) + 1   #add 1 because we're counting edges


  def getMin(self, root):
    if root == None:
      raise ValueError("Error: tree is empty")
    if root._left == None:
      return root._data
    return self.getMin(root._left)


  def getMax(self, root):
    if root == None:
      raise ValueError("Error: tree is empty")
    if root._right == None:
      return root._data
    return self.getMax(root._right)


  def _isBinarySearchTree(self, root, Q):
    """
    Called by isBinarySearchTree. Performs Breadth-First Search to visit all elements in the
    tree and checks that each value meets the constraints of a BST. The function
    stops as soon as a value does not meet the properties of a BST and returns false.
    We use a queue (using a deque container datatype) to traverse the tree.
    """
    if root._left != None:
      if root._data > root._left._data:
        Q.append(root._left)
      else:
        return False
    if root._right != None:
      if root._data < root._right._data:
        Q.append(root._right)
      else:
        return False
    if len(Q) == 0:
      return True
    nextNode = Q.popleft()  #get next node in the queue
    return self._isBinarySearchTree(nextNode, Q)


  def isBinarySearchTree(self, root):
    """
    Calls private function _isBinarySearchTree to determine if
    the tree is a valid BST.
    """
    if root == None:
      raise ValueError("Error: tree is empty")
    Q = deque()
    return self._isBinarySearchTree(root, Q)


  def deleteValue(self, node, value):
    if node is None:
      return node
    #find the target node
    if value < node._data:
      node._left = self.deleteValue(node._left, value)
    if value > node._data:
      node._right = self.deleteValue(node._right, value)
    else:     #value has been found!
      #case 1: node has no children
      if node._left is None and node._right is None:
        node = None
      #case 2: only 1 child
      elif node._right is None:
        node = node._left
      elif node._left is None:
        node = node._right
      else:
        """case 3: the node has 2 children: replace the target node with its predecessor,
        i.e. the max valued node of its left sub-tree:
          1. find predecessor
          2. replace the data on the target node w/the data from predecessor
          3. set the left sub-tree of the target node to the result of deleting the now
             duplicated node (i.e. the predecessor). Start from the target node's left
             child, looking for the duplicate value of the data.
        """
        predecessor = self.getMax(node._left)
        node._data = predecessor._data
        node._left = self.deleteValue(node._left, predecessor._data)
    return node


  def getSuccessor(self, root, value):
    """
    If the node has a right sub-tree, the successor is the min value of the node's right sub-tree
    Otherwise, we need to find the deepest ancestor of which this node is on its left sub-tree
    """
    if root is None or (root._left is None and root._right is None):
      return None
    #find given node
    current = root
    while root is not None:
      if value == root._data:
        break
      if value < root._data:
        current = root._left
      elif value > root._data:
        current = root._right
    #case 1: node has a right sub-tree
    if current._right is not None:
      return self.getMin(current._right)
    #case 2: node has no right sub-tree
    else:
      successor = None
      ancestor = root
      while ancestor is not current:
        if current._data < ancestor._data:
          successor = ancestor          #so far this is the deepest node of which current is on its left
          ancestor = ancestor._left     #but keep looking on the left sub-tree
        else:
          ancestor = ancestor._right    #the current node was on the right of the ancestor, advance and keep looking left
      return successor

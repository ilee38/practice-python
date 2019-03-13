#!/usr/local/bin/python3
"""
# Test file for BinarySearchTree class
"""
from binary_search_tree import BinarySearchTree

if __name__ == "__main__":
  root = None
  bst = BinarySearchTree()

  root = bst.insert(root, 15)
  print("created node with value 15")
  root = bst.insert(root, 10)
  print("created node with value 10")
  root = bst.insert(root, 20)
  print("created node with value 20")
  root = bst.insert(root, 8)
  print("created node with value 8")
  root = bst.insert(root, 12)
  print("created node with value 12")
  root = bst.insert(root, 17)
  print("created node with value 17")
  root = bst.insert(root, 25)
  print("created node with value 25")
  root = bst.insert(root, 6)
  print("created node with value 6")
  root = bst.insert(root, 11)
  print("created node with value 11")
  root = bst.insert(root, 16)
  print("created node with value 16")
  root = bst.insert(root, 27)
  print("created node with value 27")

  print("Is current tree a BST?")
  if bst.isBinarySearchTree(root):
    print("yes")
  else:
    print("no")

  print("Printing node values in order...")
  bst.printValues(root)

  print("The minimum value in the BST is: ", bst.getMin(root))
  print("The maximum value in the BST is: ", bst.getMax(root))

  print("Tree's height is: ", bst.getHeight(root))

  print("Checking if 17 is in tree: ")
  if bst.isInTree(root, 17):
    print("found it!")
  else:
    print("value not found in tree")
  print("Checking if 150 is in tree (it should not be): ")
  if bst.isInTree(root, 150):
    print("found it!")
  else:
    print("value not found in tree")

  print("Get successor of 25: ", bst.getSuccessor(root, 25))
  print("Get successor of 17: ", bst.getSuccessor(root, 17))

  print("Deleting 6...")
  bst.deleteValue(root, 6)
  bst.printValues(root)
  print("The minimum value in the BST is: ", bst.getMin(root))
  print("The maximum value in the BST is: ", bst.getMax(root))
  print("Deleting 12...")
  bst.deleteValue(root, 12)
  bst.printValues(root)
  print("Deleting 20...")
  bst.deleteValue(root, 20)
  bst.printValues(root)
  print("Deleting 27...")
  bst.deleteValue(root, 27)
  bst.printValues(root)
  print("The minimum value in the BST is: ", bst.getMin(root))
  print("The maximum value in the BST is: ", bst.getMax(root))

  print("Deleting tree...")
  root = bst.deleteTree(root)
  print(root is None)





#!usr/bin/env python3

""" Implementation of problem 2.2 from CTCI book:
    Return kth to last element (from a linked list)
"""

class Node:
  def __init__(self, val):
    self.next = None
    self.val = val


def getKth(head, k):
  if k < 1:
    raise ValueError('Value of k is invalid')
  current = head
  nodeCount = 0
  while current != None:
    nodeCount += 1
    current = current.next
  if k > nodeCount:
    raise ValueError('Value of k is greater than number of elemens in list')
  kthNode = head
  for i in range(nodeCount - k):
    kthNode = kthNode.next
  return kthNode


def main():
    head = Node(5)
    e1 = Node(3)
    e2 = Node(1)
    e3 = Node(56)
    e4 = Node(8)
    e5 = Node(23)
    head.next = e1
    e1.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    print('List:')
    current = head
    while current != None:
      print(current.val)
      current = current.next

    k = 3
    kth = getKth(head, k)
    print('kth to last element (k =',k,'):', kth.val)


if __name__ == '__main__':
  main()
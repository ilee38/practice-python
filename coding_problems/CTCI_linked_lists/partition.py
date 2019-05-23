#!/usr/bin/env python3

""" Implementation of problem 2.4 from CTCI:
    Partition linked list around value x
"""

class Node:
  def __init__(self, val):
    self.next = None
    self.val = val


def partition(head, x):
  """ Partitions linked list around element with value x
      Arguments:
      head: head node
      x: value of node to partition around
  """
  p1 = head
  p2 = None
  while p1.val >= x:
    p1 = p1.next
    if p1 == None:
      raise ValueError('value not found in list')
  p2 = p1.next
  temp = head.val
  head.val = p1.val
  p1.val = temp
  p1 = head     #reset p1
  while p2 != None:
    if p2.val < x:
      temp = p1.next.val
      p1.next.val = p2.val
      p2.val = temp
      p1 = p1.next
    p2 = p2.next


def main():
  head = Node(3)
  e1 = Node(5)
  e2 = Node(8)
  e3 = Node(5)
  e4 = Node(10)
  e5 = Node(2)
  e6 = Node(1)
  head.next = e1
  e1.next = e2
  e2.next = e3
  e3.next = e4
  e4.next = e5
  e5.next = e6
  print('List:')
  current = head
  while current != None:
    print(current.val)
    current = current.next

  partition(head, 5)
  current = head
  print('Partitioned list:')
  while current != None:
    print(current.val)
    current = current.next

if __name__ == '__main__':
  main()
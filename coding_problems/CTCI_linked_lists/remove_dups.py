#!/usr/bin/env python3
""" Implementation of problem 2.1 from CTCI book:
    Remove Dups
"""

class Node:
  def __init__(self, val):
    self.next = None
    self.val = val


def removeDup(head):
  p1 = head
  p2 = head.next
  p2Prev = head
  while p1.next != None:
    while p2.next != None:
      if p1.val == p2.val:
        p2Prev.next = p2.next
        p2 = p2.next
      else:
        p2 = p2.next
        p2Prev = p2Prev.next
    if p1.val == p2.val:
      p2Prev.next = p2.next
    if p1.next != None:
      p1 = p1.next
      p2 = p1.next
      p2Prev = p1
  return head


def main():
  head = Node(5)
  e1 = Node(3)
  e2 = Node(1)
  e3 = Node(5)
  e4 = Node(8)
  e5 = Node(1)
  head.next = e1
  e1.next = e2
  e2.next = e3
  e3.next = e4
  e4.next = e5
  print('before:')
  current = head
  while current.next != None:
    print(current.val)
    current = current.next
  print(current.val)

  print('after:')
  head = removeDup(head)
  current = head
  while current.next != None:
    print(current.val)
    current = current.next
  print(current.val)


if __name__ == '__main__':
  main()

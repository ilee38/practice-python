#!/usr/bin/env python3

""" Implementation of problem 2.5 from the CTCI book
    Sum Lists
"""

class Node:
  """ class representing an linked-list node
  """
  def __init__(self, val):
    self.next = None
    self.val = val


def sumLists(head1, head2):
  """ Sums two numbers represented by a linked list, where each node contains a
      single digit. They are stored in reverse order (i.e. the 1's digit at the head,
      then the 10's digit and so on)
      Returns: the sum as a linked list
  """
  head3 = Node(0)
  current1 = head1
  current2 = head2
  current3 = head3
  carry = 0
  while current1 != None and current2 != None:
    posDigit = (current1.val + current2.val + carry) % 10
    carry = (current1.val + current2.val + carry) // 10
    current3.val = posDigit
    current3.next = Node(0)
    current1 = current1.next
    current2 = current2.next
    current3 = current3.next
  while current2 != None:
    current3.val = current2.val
    current2 = current2.next
    current3.next = Node(0)
    current3 = current3.next
  while current1 != None:
    current3.val = current1.val
    current1 = current1.next
    current3.next = Node(0)
    current3 = current3.next
  current3 = None
  return head3


def main():
  list1 = Node(7)
  e1 = Node(1)
  e2 = Node(6)
  list1.next = e1
  e1.next = e2
  list2 = Node(5)
  e3 = Node(9)
  e4 = Node(2)
  list2.next = e3
  e3.next = e4

  list3 = sumLists(list1, list2)
  current = list3
  while current != None:
    print(current.val)
    current = current.next

if __name__ == '__main__':
  main()
#!/usr/bin/env python3
""" Problem 2.7 from CtCI book
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def intersection(H1, H2):
  if H1 is None or H2 is None:
    return None
	#to do, check if only 1 element
  h1_length = 1
  h2_length = 1
  ptr1 = H1
  ptr2 = H2

  while ptr1.next is not None:
    ptr1 = ptr1.next
    h1_length += 1
  while ptr2.next is not None:
    ptr2 = ptr2.next
    h2_length += 1

  if ptr1 is not ptr2:
    return None
  else:
    ptr1 = H1
    ptr2 = H2
    offset = h1_length - h2_length
    if offset > 0:
      for i in range(0, offset):
        ptr1 = ptr1.next
    elif offset < 0:
      for i in range(0, abs(offset)):
        ptr2 = ptr2.next
    elif offset == 0:
      return ptr1

    while ptr1 is not ptr2:
      ptr1 = ptr1.next
      ptr2 = ptr2.next
    return ptr1


def main():
  """
    a->b->c
    m->j->b->c
  """
  a = Node('a')
  b = Node('b')
  c = Node('c')
  m = Node('m')
  j = Node('j')
  a.next = b
  b.next = c
  m.next = j
  j.next = b

  h1 = a
  h2 = m
  intersect = intersection(h1, h2)
  print(intersect.val)

if __name__ == '__main__':
  main()

#!/usr/bin/env python3

""" Problem 2.6 from CtCI book
"""
from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def check_palindrome(head):
  if head is None:
    return None
  elif head.next is None:
    return True
  else:
    st = deque()
    current = head
    while current is not None:
      if current.val != " ":
        st.append(current.val.lower())
      current = current.next

    current = head
    while current is not None:
      if current.val == " ":
        current = current.next
      if current.val.lower() != st.pop():
        return False
      else:
        current = current.next
    return True


def main():
  t = Node("t")
  a = Node("a")
  c = Node("c")
  o = Node("o")
  sp = Node(" ")
  c1 = Node("c")
  a1 = Node("a")
  t1 = Node("t")
  t.next = a
  a.next = c
  c.next = o
  o.next = sp
  sp.next = c1
  c1.next = a1
  a1.next = t1
  print(check_palindrome(t))

if __name__ == '__main__':
  main()

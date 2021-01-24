#!/usr/bin/env python3

class Node:
   def __init__(self, value):
      self.value = value
      self.next = None


"""
   Note: In this case, we defined k in the following manner:
   k = 0 will return the last element, k = 1 will return the first to last,
   k = 2 the second to last and so on.
"""
def kth_to_last(head, k):
   length = 0
   node = head
   while node is not None:
      length += 1
      node = node.next
   if length < k+1:
      return None

   node = head
   for _ in range(1, length - k):
      node = node.next
   return node


def main():
   a = Node('a')
   b = Node('b')
   c = Node('c')
   d = Node('d')
   e = Node('e')
   aa = Node('aa')
   bb = Node('bb')
   dd = Node('dd')

   a.next = b
   b.next = c
   c.next = d
   d.next = aa
   aa.next = bb
   bb.next = e
   e.next = dd

   n = kth_to_last(a, 3)
   print(n.value)


if __name__ == '__main__':
   main()
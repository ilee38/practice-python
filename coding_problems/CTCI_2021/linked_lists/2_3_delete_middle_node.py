#!/usr/bin/env python3
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

def del_middle_node(node):
   """ Copy the next node to the middle node, then delete the next node.
   """
   next_node = node.next
   node.value = next_node.value
   node.next = next_node.next
   next_node.next = None


def main():
   a = Node('a')
   b = Node('b')
   c = Node('c')
   d = Node('d')
   e = Node('e')
   f = Node('f')

   a.next = b
   b.next = c
   c.next = d
   d.next = e
   e.next = f

   n = a
   while n is not None:
      print(n.value)
      n = n.next

   del_middle_node(c)
   n = a
   while n is not None:
      print(n.value)
      n = n.next


if __name__ == '__main__':
   main()
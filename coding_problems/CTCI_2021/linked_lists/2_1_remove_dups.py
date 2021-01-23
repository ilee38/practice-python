#!/usr/bin/env python3

class Node:
   def __init__(self, value):
      self.value = value
      self.next = None


""" Solution 1: using extra memory
"""
def remove_dups(head):
   seen = set()
   element = head
   previous = None
   while element is not None:
      if element.value in seen:
         # Remove element from the list
         previous.next = element.next
      else:
         seen.add(element.value)
         previous = element
      element = element.next
   return head


""" Solution 2: In-place
"""
def remove_dups_in_place(head):
   curr_element = head
   runner = curr_element.next
   previous = curr_element
   while curr_element.next is not None:
      while runner is not None:
         if curr_element.value == runner.value:
            previous.next = runner.next
         else:
            previous = runner
         runner = runner.next
      curr_element = curr_element.next
      runner = curr_element.next
   return head


def main():
   a = Node('a')
   b = Node('b')
   c = Node('c')
   d = Node('d')
   e = Node('e')
   aa = Node('a')
   bb = Node('b')
   dd = Node('d')

   a.next = b
   b.next = c
   c.next = d
   d.next = aa
   aa.next = bb
   bb.next = e
   e.next = dd

   head = remove_dups(a)
   n = head
   while n is not None:
      print(n.value, end='')
      n = n.next
   print('\n')

   a.next = b
   b.next = c
   c.next = d
   d.next = aa
   aa.next = bb
   bb.next = e
   e.next = dd

   head_2 = remove_dups_in_place(a)
   n = head_2
   while n is not None:
      print(n.value, end='')
      n = n.next
   print('\n')


if __name__ == '__main__':
   main()
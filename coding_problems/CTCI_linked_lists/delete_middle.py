#!/usr/bin/env python3
""" Problem 2.3 in CtCI book
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def del_middle(mid):
  if mid == None or mid.next == None:
    return

  mid.val = mid.next.val
  mid.next = mid.next.next


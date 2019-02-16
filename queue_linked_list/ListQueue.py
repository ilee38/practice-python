#!/usr/local/bin/python3

###
# Implementation of a Queue using a linked list with tail pointer
###
from ListNode import ListNode

class ListQueue:

  def __init__(self):
    self._head = None        #Initially, the queue is empty
    self._tail = None
    self._size = 0


  def enqueue(self, val):
    newNode = ListNode(val, None)
    if self._size == 0:
      self._tail = newNode
      self._head = newNode
    else:
      self._tail.set_next(newNode)    #Add element to the back and update tail
      self._tail = newNode
    self._size += 1


  def dequeue(self):
    if self._size == 0:
      raise ValueError("Queue is empty")
    retVal = self._head.get_value()
    if self._size == 1:             #If only 1 element, set head and tail to None
      self._head = None
      self._tail = None
    else:
      self._head = self._head.get_next()    #otherwise, update head
    self._size -= 1
    return retVal


  def empty(self):
    return self._size == 0
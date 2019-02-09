#!/usr/local/bin/python3

"""
# Definition of SinglyLinkedList class. This list keeps track of the
# tail pointer and the size of the list.
"""
from ListNode import ListNode

class SinglyLinkedList:

  def __init__(self):
    self._head = None
    self._tail = None
    self._size = 0


  # Returns the size (number of elements) of the list
  def size(self):
    return self._size


  # Returns boolean value indicating if the list is currently empty
  def empty(self):
    if self._size == 0:
      return True
    return False


  # Returns the value of item at index (starting from 0)
  def value_at(self, index):
    if index >= self._size or index < 0:
      raise IndexError('Invalid index')
    item = self._head
    for i in range(index):    #traverse the list to find the item
      item = item.get_next()
    return item.get_value()


  # Adds an item to the front of the list
  def push_front(self, val):
    newNode = ListNode(val, None)
    if self._size == 0:           #if list is empty, make element the head and tail
      self._head = newNode
      self._tail = newNode
    newNode.set_next(self._head)  #new element's next now points to current head
    self._head = newNode          #update list's head
    self._size += 1               #update list's size


  # Removes the front item and returns its value
  def pop_front(self):
    if self._size == 0:
      raise ValueError('List is empty')
    retVal = self._head.get_value()
    if self._size == 1:               #if list has only 1 element, set head and tail to None
      self._head = None
      self._tail = None
    else:
      self._head = self._head.get_next()    #update list head
    self._size -= 1
    return retVal


  # Adds an item to the end of the list
  def push_back(self, val):
    newNode = ListNode(val, None)
    if self._size == 0:
      self._head = newNode
      self._tail = newNode
    self._tail.set_next(newNode)    #current tail now points to new item
    self._tail = newNode            #make the new item the tail
    self._size += 1


  # Removes the last item and returns its value
  def pop_back(self):
    if self._size == 0:
      raise ValueError('List is empty')
    retVal = self._tail.get_value()
    if self._size == 1:             #case were there's only 1 element
      self._head = None
      self._tail = None
    else:
      item = self._head
      for i in range(self._size - 1):   #traverse the list to find the second to last item
        item = item.get_next()          #and set it as the new tail
      item.set_next(None)
      self._tail = item
    self._size -= 1
    return retVal


  # Returns the value of the front item
  def front(self):
    return self._head.get_value()


  # Returns the value of the end item
  def back(self):
    return self._tail.get_value()


  # Inserts value at index, so current item at that index is pointed to by new
  # item at that index. We assume that the list has at least 2 items (otherwise
  # the user should call the push_front() or push_back() methods)
  def insert(self, index, val):
    if index >= self._size or index < 0:
      raise IndexError('Invalid index')
    if index == 0:
      self.push_front(val)
    else:
      newNode = ListNode(val, None)
      item = self._head
      for i in range(index - 1):    #traverse list to find item at index - 1
        item = item.get_next()
      newNode.set_next(item.get_next())
      item.set_next(newNode)
    self._size += 1


  # Removes node at given index
  def erase(self, index):
    if self._size == 0:
      raise ValueError('List is empty')
    elif index >= self._size or index < 0:
      raise IndexError('Invalid index')
    if index == 0:
      self.pop_front()                #special cases where items are the head or the
    elif index == self._size - 1:     #tail of the list
      self.pop_back()
    else:
      item = self._head
      for i in range(index - 1):      #traverse list to get node at index-1
        item = item.get_next()
      toDelete = item.get_next()
      item.set_next(toDelete.get_next())  #update next pointer of the element at index-1
    self._size -= 1
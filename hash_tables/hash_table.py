#!/usr/local/bin/python3

"""
# Implementation of a HashTable class using Linear Probing with Multiply Add and
# Divide (MAD) compression function
"""
from hash_item import HashItem
from random import randrange

class HashTable:
  _LOAD_FACTOR_THR = 0.5      #Threshod for load factor
  _AVAIL = object()           #Empty object to indicate deleted items


  # Initial capacity is set to 11 (a prime number to improve collisions)
  # parameter p is a prime number greater than the size of the underliying
  # "bucket" array. It is used for MAD compression.
  def __init__(self, cap=11, p=10934521):
    self._n = 0.0     #number of stored elements used to calculate the load factor
    self._table = [None] * cap    #using a Python list as underlying array
    self._prime = p
    self._a = 1 + randrange(p-1)
    self._b = randrange(p)


  def _len(self):
    return self._n


  # Returns the index corresponding to the given key.
  # This function makes use of python's hash() function to generate a hash code
  # for the key, it then compresses the value to a number in the range [0, N-1]
  # using MAD (N is the capacity of the underlying array).
  def _hash(self, key, N):
    j = hash(key)         #get hash code for key
    return ((self._a*j + self._b) % self._prime) % N


  # Each time the hash table is resized, a new index has to be computed for each
  # existing element's key based on the new capacity of the table.
  def _resize(self, newCap):
    B = [None] * newCap
    elements = []
    for i in range(len(self._table)):
      if self._table[i] is not None or self._table[i] is not HashTable._AVAIL:
        elements.append(self._table[i])
    for e in elements:
      newIndex = self._hash(e.get_key(), newCap)
      B[newIndex] = e
    self._table = B


  def _is_available(self, index):
    return self._table[index] is None or self._table[index] is HashTable._AVAIL


  # Looks for key starting from given index.
  # Returns a tuple (boolean, index) indicating if key was found and its index,
  # or if the key is not found, parameter index indicates the 1st available slot.
  # When searching for a key, if we encouter an _AVAIL element, we still keep looking
  # since that indicates that element was recently deleted.
  def _find_slot(self, index, key):
    availableIdx = None
    while True:
      if self._is_available(index):
        if availableIdx is None:      #availableIdx keeps track of 1st available slot
          availableIdx = index        #we only update it if it hasn't been assigned
        if self._table[index] is None:
          return (False, index)
      elif self._table[index].get_key == key:
        return (True, index)
      index = (index + 1) % len(self._table)  #keep looking to next index.


  def get(self, k):
    i = self._hash(k, len(self._table))
    found, index = self._find_slot(i, k)
    if not found:
      raise ValueError("Error: key not found in table")
    return self._table[index].get_value()


  def add(self, k, v):
    newItem = HashItem(k, v)
    i = self._hash(k, len(self._table))
    found, index = self._find_slot(i, k)
    if found:
      self._table[index].set_value(v)
      newItem = None
    else:
      self._table[index] = newItem
      self._n += 1.0
      if (self._n/len(self._table)) > HashTable._LOAD_FACTOR_THR:
        self._resize(2*len(self._table))


  def remove(self, k):
    i = self._hash(k, len(self._table))
    found, index = self._find_slot(i, k)
    if not found:
      raise ValueError("Error: key not found in table")
    else:
      self._table[index] = HashTable._AVAIL
      self._n -= 1.0


  def exists(self, key):
    i = self._hash(key, len(self._table))
    found, j = self._find_slot(i, key)
    return found
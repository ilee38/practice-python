#!/usr/bin/env python3
""" Problem 3.6 from the CtCI book
"""
from collections import deque

class PetQueue:

  def __init__(self):
    self._cat_q = deque()
    self._dog_q = deque()
    self._timer = 0


  def enqueue(self, pet_type):
    new_pet = (pet_type, self._timer)
    if pet_type.lower() == 'dog':
      self._dog_q.append(new_pet)
      self._timer += 1
    elif pet_type.lower() == 'cat':
      self._cat_q.append(new_pet)
      self._timer += 1
    else:
      raise ValueError('Invalid pet type')


  def dequeueAny(self):
    if len(self._dog_q) == 0 and len(self._cat_q) == 0:
      raise ValueError('No pets left')
    if len(self._cat_q) == 0:
      return self._dog_q.popleft()
    if len(self._dog_q) == 0:
      return self._cat_q.popleft()

    dog, dog_time = self._dog_q.popleft()
    cat, cat_time = self._cat_q.popleft()
    if dog_time < cat_time:
      self._cat_q.appendleft((cat, cat_time))   #return cat to front of Q
      return dog, dog_time
    else:
      self._dog_q.appendleft((dog, dog_time))   #return dog to front of Q
      return cat, cat_time


  def dequeueCat(self):
    if len(self._cat_q) == 0:
      raise ValueError('No cats left')
    return self._cat_q.popleft()


  def dequeueDog(self):
    if len(self._dog_q) == 0:
      raise ValueError('No dogs left')
    return self._dog_q.popleft()

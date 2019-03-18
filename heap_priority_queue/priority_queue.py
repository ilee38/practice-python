#!/usr/local/bin/python3
"""
Implementation of a Priority Queue using an array-based Max-Heap
"""

class PriorityQueue:

  class HeapNode:
    """ Nested class representing an element in the Heap """
    __slots__ = "key", "value"

    def __init__(self, k, val):
      self.key = k
      self.value = val

  def __init__(self, cap):
    self._capacity = cap          #capacity of the array
    self._size = 0                #number of elements in the queue
    self._PQ_data = [None]*cap    #array (list) holding the data


  def insert(self, k, val):
    """ Inserts a new element into the priority queue:
    1. insert the new element  at the end of the array, then
    2. sift up the element to fix the heap (if needed)
    """
    if self._size == self._capacity:
      raise ValueError("Error: queue is full")
    node = self.HeapNode(k, val)
    self._PQ_data[self._size] = node
    self._size += 1
    self._sift_up(self._size - 1)


  def _sift_up(self, pos):
    """ Sifts up the element at the given position:
    1. compare element with its parent and
    2. if element is greater, swap it with the parent
    3. repeat process until reaching the top of the heap
    """
    if pos <= 0:
      return
    parent = (pos - 1) // 2
    if self._PQ_data[pos].key > self._PQ_data[parent].key:
      temp = self._PQ_data[parent]
      self._PQ_data[parent] = self._PQ_data[pos]
      self._PQ_data[pos] = temp
    else:
      return
    self._sift_up(parent)


  def get_max(self):
    """ Returns the element (w/out removing it) with the maximum value in the
    priority queue. I.e. the element at the top of the heap.
    """
    return self._PQ_data[0]


  def get_size(self):
    """ Returns the number of elements in the priority queue """
    return self._size


  def is_empty(self):
    return self._size == 0


  def extract_max(self):
    """ Returns and removes the element with the greatest key in the priority queue.
    I.e. the element at the top of the heap. To remove the top element:
    1. Replace the top element with the last element in the array (deleting the last element)
    2. Then sift down the element to fix the heap.
    """
    max_element = self._PQ_data[0]
    self._PQ_data[0] = self._PQ_data[self._size - 1]
    self._size -= 1
    self._sift_down(0)
    return max_element


  def _sift_down(self, pos):
    """ Sifts the element at the given position down the heap to maintain the
    Max Heap order property:
    1. Compare the element's key with its children's keys. If the element's key is
    lower, then choose the child with the greatest key value and swap them (first
    check if the element has left and/or right children)
    2. Continue until reaching the end of the Heap.
    """
    if (2*pos + 1) >= self._size:
      return
    max_pos = pos
    l_child = 2*pos + 1
    r_child = 2*pos + 2
    # check if there are left and/or right children and compare keys
    if (l_child <= self._size) and (self._PQ_data[max_pos].key < self._PQ_data[l_child].key):
      max_pos = l_child
    if (r_child <= self._size) and (self._PQ_data[max_pos].key < self._PQ_data[r_child].key):
      max_pos = r_child
    if max_pos != pos:
      temp = self._PQ_data[pos]
      self._PQ_data[pos] = self._PQ_data[max_pos]
      self._PQ_data[max_pos] = temp
      self._sift_down(max_pos)


  def remove(self, index):
    """ Removes item at given index from the array
    1. Swap with last element, then
    2. sift down
    """
    self._PQ_data[index] = self._PQ_data[self._size - 1]
    self._size -= 1
    self._sift_down(index)


  def heapify(self, arr, count):
    """ Creates a Heap from an array of elements (integers). Needed for heap sort.
    1. Start from the first non-leaf node (i.e. position [(n-1)/2]-1) going up.
    2. Call sift_down() for each of these nodes.

    Parameters:
    arr = array of integers
    conut = number of elements in the array
    """
    for i in range((count-1)/2 - 1, -1, -1):
      self._int_sift_down(arr, i, count)


  def heap_sort(self, arr, count):
    """ Performs in-place heap-sort algorithm on an array of elements.
    1. Make the array a Max Heap
    2. Since the max element is always at the top, we swap the first and last
    elements in the array (n-1) times. (this puts the max element at the end of the array)
    3. Each time we swap the elements, we "decrease" the array's size and call sift_down.

    Parameters:
    arr = array of integers
    conut = number of elements in the array
    """
    temp = None
    self.heapify(arr, count)
    for i in range(count - 1, 0, -1):
      temp = arr[i]
      arr[i] = arr[0]
      arr[0] = temp
      # before calling sift_down, "decrease" the array size (i.e. the last index is now i-1)
      self._int_sift_down(arr, 0, i-1)


  def _int_sift_down(self, arr, pos, size):
    """ Perform sift down for an array of integers
    Takes an array of values, a position, and the size of the array (i.e.
    the number of elements in the array)
    """
    if (2*pos + 1) > size:
      return
    max_pos =  pos
    l_child = 2*pos + 1
    r_child = 2*pos + 2
    if (l_child <= size) and (arr[max_pos] < arr[l_child]):
      max_pos = l_child
    if (r_child <= size) and (arr[max_pos] < arr[r_child]):
      max_pos = r_child
    if max_pos != pos:
      temp = arr[pos]
      arr[pos] = arr[max_pos]
      arr[max_pos] = temp
    self._int_sift_down(arr, max_pos, size)
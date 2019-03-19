#!/usr/local/bin/python3
""" Test file for PriorityQueue class """

from priority_queue import PriorityQueue

if __name__ == '__main__':
  PQ = PriorityQueue(10)

  print("Created new priority queue, current size is: ", PQ.get_size())
  print("Is the queue empty? ", PQ.is_empty())
  print("Inserting 6 elements... ")
  PQ.insert(23, "Hello")
  PQ.insert(98, "world!")
  PQ.insert(186, "I'm")
  PQ.insert(12, "in")
  PQ.insert(354, "a")
  PQ.insert(6, "queue")
  print("Done, current size is: ", PQ.get_size())
  print("Is the queue empty? ", PQ.is_empty())
  print("Max element is: ", PQ.get_max().key, " ", PQ.get_max().value)
  max_element = PQ.extract_max()
  print("Removing max element...", max_element.get_key(), " ", max_element.get_value())
  print("Done, current size is: ", PQ.get_size())
  print("Max element is now: ", PQ.get_max().key, " ", PQ.get_max().value)
  print("Removing element at position 2...")
  PQ.remove(2)
  print("Done, current size is: ", PQ.get_size())

  unsorted_list = [613, 55, 8721, 472, 94, 72, 74, 8, 61, 356]
  print("Printing unsorted array...")
  for num in unsorted_list:
    print(num)
  print("Sorting the array with Heap-Sort...")
  PQ.heap_sort(unsorted_list, 10)
  print("Printing sorted array...")
  for num in unsorted_list:
    print(num)
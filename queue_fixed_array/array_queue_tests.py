#!/usr/local/bin/python3

"""
# Tests for queue implementation using an underlying fixed-size array
"""
from ArrayQueue import ArrayQueue

if __name__ == '__main__':
  q = ArrayQueue()

  print("Is queue empty: ")
  if q.empty():
    print("yes")
  else:
    print("no")
  print("Enqueueing 9...")
  q.enqueue(9)
  print("Is queue empty: ")
  if q.empty():
    print("yes")
  else:
    print("no")
  print("Dequeueing... ")
  print(q.dequeue())
  print("Enqueueing 45, 53, and 85...")
  q.enqueue(45)
  q.enqueue(53)
  q.enqueue(85)
  print("Now dequeueing all of them...")
  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())
  print("Is queue empty: ")
  if q.empty():
    print("yes")
  else:
    print("no")


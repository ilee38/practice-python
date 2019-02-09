#!/usr/local/bin/python3

from SinglyLinkedList import SinglyLinkedList

if __name__ == '__main__':
  ll = SinglyLinkedList()

  print("initial size: ", ll.size())
  print("is list empty? ")
  if ll.empty():
    print("yes")
  else:
    print("no")
  print("pushing 24 to front...")
  ll.push_front(24)
  print("new size: ", ll.size())
  print("value at index 0: ", ll.value_at(0))
  print("pushing 6 at back...")
  ll.push_back(6)
  print("value at index 0: ", ll.value_at(0))
  print("value at index 1: ", ll.value_at(1))
  print("now pushing 783 at front...")
  ll.push_front(783)
  print("new size: ", ll.size())
  print("value at index 0: ", ll.value_at(0))
  print("value at index 1: ", ll.value_at(1))
  print("value at index 2: ", ll.value_at(2))
  print("front value: ", ll.front())
  print("back value: ", ll.back())
  print("inserting 4 at index 1...")
  ll.insert(1,4)
  print("value at index 1: ", ll.value_at(1))
  print("value at index 2: ", ll.value_at(2))
  print("front value: ", ll.front())
  print("back value: ", ll.back())
  print("popping from front...", ll.pop_front())
  print("popping from back...", ll.pop_back())
  print("pushing 18 to front...")
  ll.push_front(18)
  print("erasing node at index 1...")
  ll.erase(1)
  print("new value at index 1: ", ll.value_at(1))
  print("new size: ", ll.size())

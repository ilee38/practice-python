#!/usr/local/bin/python3

from hash_table import HashTable

if __name__ == '__main__':
  ht = HashTable()

  print("Current number of elements: ", ht._n)
  print("Current table capacity: ", len(ht._table))
  print("Adding (1, one) pair...")
  ht.add(1, "one")
  print("Adding (2, two) pair...")
  ht.add(2, "two")
  print("Adding (3, three) pair...")
  ht.add(3, "three")
  print("Current number of elements: ", ht._n)
  print("Does key 2 exists?")
  if ht.exists(2):
    print("yes")
  else:
    print("no")
  print("Get value of key 1: ", ht.get(1))
  print("Get value of key 2: ", ht.get(2))
  print("Get value of key 3: ", ht.get(3))
  print("Removing element with key 2")
  ht.remove(2)
  print("Does key 2 exists?")
  if ht.exists(2):
    print("yes")
  else:
    print("no")
  print("Adding elements to force table resizing...")
  ht.add(4,"four")
  ht.add(5,"five")
  ht.add(6,"six")
  ht.add(7,"seven")
  ht.add(8,"eight")
  ht.add(9,"nine")
  ht.add(10,"ten")
  print("Current number of elements: ", ht._n)
  print("Current table capacity: ", len(ht._table))
  print("Get value of key 1: ", ht.get(1))
  print("Get value of key 3: ", ht.get(3))
  print("Get value of key 4: ", ht.get(4))
  print("Get value of key 10: ", ht.get(10))
  print("Get value of key 9: ", ht.get(9))
  print("Get value of key 8: ", ht.get(8))
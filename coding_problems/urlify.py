#!/usr/bin/env python3

def URLify(text, size):
  #todo: verify inputs
  w_s = " "
  newSize = size
  for i in range(size):
    if text[i] == w_s:
      makeRoom(text, i, newSize)
      text[i] = "%"
      text[i+1] = "2"
      text[i+2] = "0"
      i += 3
      newSize += 2
  return text


def makeRoom(text, i, size):
  """ Shift string right by 2 positions each time a white space is found
  """
  last = size - 1
  for j in range(size-1, i, -1):
    text[last+2] = text[j]
    last -= 1


if __name__ == '__main__':
  string = "Mr John Smith    "
  length = 13
  urlStr = URLify(list(string), length)
  print(str(urlStr))
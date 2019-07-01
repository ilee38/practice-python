#!/usr/bin/env python3
""" Problem 3.5 from CtCI book
"""
from collections import deque

def sort_stack(main_st):
  temp_st = deque()
  count = 0
  temp_st.append(main_st.pop())
  while len(main_st) > 0:
    tmp = main_st.pop()
    length = len(temp_st)
    for i in range(length):
      if tmp > peek(temp_st):
        main_st.append(temp_st.pop())
        count += 1
      else:
        temp_st.append(tmp)
        tmp = None
        break
    if tmp is not None:
      temp_st.append(tmp)
      tmp = None
    for i in range(count):
      temp_st.append(main_st.pop())
    count = 0
  return temp_st


def peek(st):
  val = st.pop()
  st.append(val)
  return val
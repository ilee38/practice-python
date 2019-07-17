#!/usr/bin/env python3
def longest_subseq(S, D):
  """ Find the longest word in a dictionary that is a subsequence
      of a given string.
      args:
        S string
        D list of strings
  """
  if len(S) == 0 or len(D) == 0:
    return None
  max_len = 0
  longest = ''
  for word in D:
    start_idx = 0
    valid_word = True
    if len(word) <= len(S) and len(word) > max_len:
      for i in range(len(word)):
        if word[i] in S[start_idx:]:
          start_idx = S.find(word[i]) + 1
        else:
          valid_word = False
          break
      if valid_word:
        max_len = len(word)
        longest = word
  return longest
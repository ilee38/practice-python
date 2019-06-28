#!/usr/bin/env python3
""" Problem 8.5 from CtCI book
"""
def rec_multiply(x, y):
	#todo validate inputs
  cache = {(1,1):1}
  sm = min(x,y)
  lrg = max(x,y)
  return _rec_multiply(sm, lrg, cache)


def _rec_multiply(sm, lrg, cache):
  if sm == 0 or lrg == 0:
    return 0

  if (sm,lrg) in cache.keys():
    return cache[(sm,lrg)]

  if sm%2 == 0 and lrg%2 == 0:    #both are even
    half = _rec_multiply(lrg//2, sm, cache)
    cache[(sm,lrg)] = half + half
    return cache[(sm,lrg)]
  elif lrg%2 != 0 and sm%2 != 0:  #both are odd
    lrg1 = lrg//2
    lrg2 = lrg-lrg1
    result = _rec_multiply(lrg1, sm, cache) + _rec_multiply(lrg2, sm, cache)
    cache[(sm,lrg)] = result
    return cache[(sm,lrg)]
  elif lrg%2 != 0 and sm%2 == 0:    #only sm is odd
    half = _rec_multiply(lrg, sm//2, cache)
    cache[(sm,lrg)] = half + half
    return cache[(sm,lrg)]
  else:                       #only lrg is odd
    half = _rec_multiply(lrg//2, sm, cache)
    cache[(sm,lrg)] = half + half
    return cache[(sm,lrg)]
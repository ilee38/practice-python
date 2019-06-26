#!/usr/bin/env python3
""" Problem 1.1 from CtCI book
"""
def check_unique(S):
	if len(S) == 1:
		return True
	elif S is None or len(S) == 0:
		return False
	new_s = ''.join(sorted(S))
	prev = 0
	for x in range(1, len(new_s)):
		if new_s[x] == new_s[prev]:
			return False
		prev += 1
	return True

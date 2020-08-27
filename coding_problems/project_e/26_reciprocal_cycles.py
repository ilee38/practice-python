#!/usr/bin/env python3

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def longest_recurring_cycle():
	''' Returns the denominator that generates the longest repeating cycle in
			the decimal 1/d, where d < 1000
	'''
	N = 1		
	longest_cycle = 0
	longest_d = 0
	result = [] 
	remainders = set()
	for d in range(2, 1000):
		while True:
			while N < d and N > 0:
				N *= 10
			if N in remainders or N == 0:
				first_idx = result.index(r)		#index of the 1st number in the cycle
				if len(result[first_idx:]) > longest_cycle:
					longest_d = d
					longest_cycle = len(result)
				break
			remainders.add(N)
			r = N // d	
			result.append(r)
			N -= (d * r)
		remainders = set()
		result = [] 
		N = 1
	return longest_d		# That's what she said :)


def main():
	print(longest_recurring_cycle())


if __name__ == '__main__':
	main()

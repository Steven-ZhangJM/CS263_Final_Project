
from math import floor
__author__ = "bovenson"
__date__ = "2020-07-23"



"""
Use dynamic programming to reduce the number of ways from 1 to N.
"""

def num_ways(N):
	memo = [None for i in range(51)]
	print(memo)
	
	return num_ways_helper(N,0,None,memo)

def num_ways_helper(N,position,memo,res):
	if N < 0:
		return 0

	if position!= N:
		res = memo[N]
		
	if res is None:
		if N > 4:
			if N % 5 == 0:
				res = sum([num_ways_helper(N-5,i,memo,None) for i in range(1,6)])
			elif N % 2 == 0:
				res = sum([num_ways_helper(N-2,i,memo,None) for i in range(3)])
			else:
				return sum([num
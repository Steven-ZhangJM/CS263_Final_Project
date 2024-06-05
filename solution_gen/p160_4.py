

import sys
sys.setrecursionlimit(100000)

factorial_dict = {}

def factorial(N):
	if N == 1:
		return 1
	
	if str(N) in factorial_dict:
		return factorial_dict[str(N)]
	val =  N * factorial(N-1)
	print(f"N: {N}", end=' ')
	print(f"val: {val}", end=' ')
	factorial_dict[str(N)] = val
	return val

n_str = input().strip()
total = int(n_str)
print(factorial(total))
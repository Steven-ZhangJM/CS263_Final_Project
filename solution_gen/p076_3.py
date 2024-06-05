

def d(n: int, x: int) -> int:
	"""
	:param n: int positive integer
	:param x: number sum to be found in n
	:return: int number of ways to form numbers equal to x
	"""
	if x > n:
		return 0
	elif x == n:
		return 1
	elif x % 2 == 1:
		return 0
	else:
		return d(n, x // 2) + d(n, x // 2 - 1)

# O(2^(n-1))
def num_ways(n):
	return d(n, 2)

print(num_ways(100))

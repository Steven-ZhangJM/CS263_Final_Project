


from copy import deepcopy
import math


def all_composites(low, high):
	"""
	Generator which generates all composites from low to high
	"""
	for i in range(low, high):
		for j in range(0, i):
			if modular_test(i, j) == 1:
				yield j	


def modular_test(x, y):
	"""
	Determines whether x mod y is prime
	"""
	for i in range(2, int(math.ceil(math.sqrt(y))) + 1):
		if x % i!= 0 and y % i!= 0 and x!= y:
			return False
	return True
	


def prime_prime_generator():
	"""
	Generator which yields all primes and composites 
	(from $2$ to $9$)
	"""
	count_set_prime = []
	count_set_prime = list(range(2,9 + 1))
	yield count_set_prime

	for i in range(0, len(count
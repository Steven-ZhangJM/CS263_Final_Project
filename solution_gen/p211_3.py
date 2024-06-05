
import time

def main():
	start_time = time.time()
	solution1(1000)
	solution2(1000000)
	print("--- %s seconds ---" % (time.time() - start_time))

def solution1(end_limit):
	"""Solution 1: Sieve of Eratosthenes"""
	# Create a list with all numbers up until and including limit
	numbers = list(range(2, end_limit))
	numbers.reverse()

	# For every number, if its factorial/multiplication is a perfect square, it means it's a prime number
	# So, start from 2 - 1 and go until the end-1 (since we created a list that starts backwards - since numbers list is reversed)
	for prime in numbers:
		if prime > (numbers[0] ** 2 - 1):
			break

		elif isPrime(prime):
			candidates = numbers[:prime]

			print(f'Prime = {prime}')
			print('\tSum:'+ str(sumOfSquares(prime)))
			print('

import time

# startTimer = time.time()

"""
For this question:
Problem: Given a natural number, print all prime numbers below and including that number.
"""


def problem1(n):
	from math import sqrt
	import time
	startTimer = time.time()
	list_of_primes = []
	s = 0
	for i in range(2, n, 1):
		isprime = True
		for x in range(2, int(sqrt(i)) + 1, 1):
			if i % x == 0:
		      isprime = False
		if isprime:
		    list_of_primes.append(i)
	for i in range(2, len(list_of_primes), 1):
		if list_of_primes[i] - 1 in list_of_primes:
			s = s + list_of_primes[i]

	# print("s = {0}".format(s))
	total_time = time.time() - startTimer
	# print("Elapsed time is  %f seconds." % total_time)


problem1(2000000)

# For this question:
"""
Question: Calculate the sum of primes below two million.
"""


def problem2(n):
	# import math
	from math import sqrt
	import time
	startTimer = time.time()
	sum = 0
	for i in range(2, n, 1):
		isprime = True
		for x in range(2, round(sqrt(i)) + 1, 1):
			if i % x == 0:
		          isprime = False
		if isprime:
			sum = sum + i

	# print("sum = {0}".format(sum))
	total_time = time.time() - startTimer
	# print("Elapsed time is  %f seconds." % total_time)


problem2(200000)

"""
https://github.com/GustavOliveira/Python-Pratica-05-30-2020/blob/master/Pratica02%20pratica02.py
"""

```
import math

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_list = [p for p in range(2, n) if primes[p]]
    return prime_list

def count_ways_to_sum(n, primes):
    ways = 0
    for a in primes:
        for b in primes:
            if a + b == n:
                ways += 1
    return ways

n = 2
primes = sieve_of_eratosthenes(10000)
while True:
    count = count_ways_to_sum(n, primes)
    if count > 5000:
        print("The first value which can be written as the sum of primes in over five thousand different ways is", n)
        break
    n += 1

from math import sqrt
import itertools as it


def count_prime_divisors(n):
    divisors_max = int(sqrt(n))
    divisors_range = range(2, divisors_max + 1, 2)
    divisors = 0
    for i in divisors_range:
        if n % i == 0:
            divisors += 2
    return divisors


def count_pair_primes(n, m):
    divisors_max = int(sqrt(n))
    divisors_range = range(2, divisors_max + 1)
    divisors = 0
    for i in divisors_range:
        if n % i == 0:
            divisors += 2
        elif m % i == 0:
            divisors += 2
    return divisors


if __name__ == "__main__":
    n = list(it.islice(it.count(i, 2), 1000000))
    for pair in zip(n, n[1:]
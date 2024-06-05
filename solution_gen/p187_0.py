

from math import sqrt

import pytest
from primality.algorithms import is_prime
from primality.utils import get_primes, is_prime_factor, primes_under

primes = get_primes(101)
primes_under = [prime for prime in primes if primes_below]


def primestwo(n):
    """
    n = 100000001
    n = 1000000000000
    n = 1000000000000000000
    """
    return n in primes


def is_prime_factor(num, prime=None):
    """
    Checking for primes
    2^3 = 4, 4 is divisible by 2
    4^4 = 16,
    # 5 is a prime factor
    # 2 times 2 = 4 times 4 = 8 times 8 = 16 times 16:
    """
    if prime is None:
        if is_prime_two(num):
            return True
        return False
    prime = int(prime)
    prime_factors = []

    while num % prime == 0:
        prime_factors.append(
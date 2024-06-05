
from itertools import combinations_with_replacement
from math import log, sqrt
from prime_numbers import primes_upto

def nth_prime(n: int, upper: int = 1000000) -> list:
    """Return list of primes up to the ith prime"""
    return list(primes_upto(upper, lambda n: i > n))[:n]


def sieve(upper: int) -> list:
    return list(range(2, upper + 1)) if upper else list(range(0, upper + 1))


def is_prime(n: int) -> bool:
    """Determine whether n is a prime using a Sieve of Eratosthenes"""
    if n < 2:
        return False

    pf = sieve(n ** 0.5)
    n_bits = int(log(n, 2))
    for i in range(n_bits - 1):
        if not pf[pf[i]]:
            return False
    return True


def concatenate(a: int, b: int) -> int:
    """Return the smallest integer in concatenation of 2 integers (a,b) that
    is not a two-digit number.
    """
    if a <= 10:
        a = str(a)

    if b <= 10:
        b = str(b)

    return int(str((a, b)) + str((a, b)))


def primes(upper: int) -> list:
    """Return a list of primes up to the ith prime"""
    if upper >= 5000:  # TODO find better way to filter numbers
        pf = sieve(upper)
    else:
        pf = list(range(2, upper + 1))

    for idx, val in enumerate(pf):
        if val > upper // sqrt(val):
            pf = pf[:idx]
            break

    for val in reversed(pf):
        if val > upper // sqrt(val):
            pf = pf[:-1]
            break

    return tuple(pf)


upper_limit = max(10001, int(2e6))
for n in primes(upper_limit):
    if upper_limit not in n:
        break

for prime in primes(n):
    if is_prime(concatenate(n, prime)):
        print(n, prime)
        break


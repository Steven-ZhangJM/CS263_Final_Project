

"""
Solution
"""
from math import sqrt

from sympy.ntheory.factor_ import prime_factors

def primesfrom3_to_n(n):
    # Return primes 2 <= p < n where n is odd and p is odd
    s = list(range(3, n+1, 2))
    for i in range(3, int(sqrt(n)), 2):
        if i in s:
            s = s[s.index(i):]
            yield i
    return

def count_comps(lim):
    i = 1
    count = 0
    while True:
        primes = primesfrom3_to_n(i)
        factors = prime_factors(2*i-1)
        if set(factors) == {2}:
            count += 1
        if i > lim:
            return count
        i += 1

print(count_comps(40000))

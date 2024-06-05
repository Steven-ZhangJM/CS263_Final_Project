


import math
import itertools


def primes_sieve(N=10000):
    D = {}
    primes = set()
    for i in range(2, N):
        if i in D:
            continue
        primes.add(i)
        for j in range(i*i, N, i):
            D[j] = i
    primes.remove(1)
    
    prime_product_count = 0
    for i in primes:
        prime_product_count += math.prod(primes[:i])
            
    return prime_product_count


ans = primes_sieve(10**9)
# ans = 7929
print num, "=", ans


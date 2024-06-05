from sympy import isprime
from itertools import permutations

def check_prime_pair_set(prime_set):
    return all(isprime(int(str(p[0]) + str(p[1]))) and isprime(int(str(p[1]) + str(p[0]))) for p in permutations(prime_set, 2))

primes = [3, 7, 11, 17, 19, 23, 29, 31]  # Starting list of primes
sets = []

for i in primes:
    for j in primes:
        if j > i:
            if check_prime_pair_set({i, j}):
                for k in primes:
                    if k > j:
                        if check_prime_pair_set({i, j, k}):
                            for l in primes:
                                if l > k:
                                    if check_prime_pair_set({i, j, k, l}):
                                        for m in primes:
                                            if m > l:
                                                if check_prime_pair_set({i, j, k, l, m}):
                                                    sets.append((i, j, k, l, m))

# Find the set with the lowest sum
lowest_sum = float('inf')
lowest_set = ()
for s in sets:
    if sum(s) < lowest_sum:
        lowest_sum = sum(s)
        lowest_set = s

print(lowest_set, lowest_sum)
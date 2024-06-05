import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(2, 5000) if is_prime(i)]

def get_prime_subsets(primes):
    prime_subsets = set()
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            subset_sum = sum(set([primes[i], primes[j]]))
            if is_prime(subset_sum):
                prime_subsets.add(tuple(sorted([primes[i], primes[j]])))
    for k in range(3, len(primes)):
        for l in range(k + 1, len(primes)):
            subset_sum = sum(set([primes[k], primes[l]]))
            if is_prime(subset_sum):
                prime_subsets.add(tuple(sorted([primes[k], primes[l]])))
    return prime_subsets

prime_subsets = get_prime_subsets(primes)

print(len(prime_subsets))

#

# Solution
from math import sqrt
from itertools import permutations


def _primes(n):
    is_prime = lambda p: all(p % i for i in range(2, int(sqrt(p)) + 1))

    primes = list(map(int, list(str(n))))
    for i in range(len(primes)):
        if primes[i] > 1:
            for j in range(i, len(primes)):
                if primes[j] > 1:
                    if not is_prime(int(str(primes[i]) + str(primes[j]))):
                        primes[i] = 0
                        primes[j] = 0
    primes = filter(lambda p: p > 1, primes)

    return primes


def _digits(num):
    number_of_digits = int(sqrt(num))
    tup = tuple(i for i in range(1, num + 1))
    number_of_combinations = 2**number_of_digits - 1

    if number_of_combinations!= 1:
        combinations = []
        for perm in permutations(tup, number_of_digits):
            combinations.append(int(''.join(map(str, perm))))
    else:
        combinations = range(1, num + 1)

    return combinations


primes = _primes(1000000)
primes = set(primes)
truncated_primes = []
digits = []

for prime in primes:
    if prime > 1000000:
        break
    prime_digits = _digits(prime)
    is_truncatable = True
    for digit in prime_digits:
        if not any(str(digit).startswith(pre) for pre in str(prime)):
            is_truncatable = False
    digit_sum = sum(int(s) for s in str(prime)) if is_truncatable else 0
    truncated_primes.append(prime)
    digits.append(digit_sum)

for i in range(len(truncated_primes)):
    truncated_primes[i] = str(truncated_primes[i])


# 2, 3, 5, 7 are not primes numbers.
result = (int(filter(lambda x: filter(lambda y: x % y > 0, truncated_primes), digits)))

# 2: 97 and 97: 7
print((sum(int(x[:2]) for x in truncated_primes)))

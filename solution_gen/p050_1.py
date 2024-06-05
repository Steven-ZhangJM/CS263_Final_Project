

import time
from math import sqrt
from Prime import primes_until


def largest_prime_sum_above(n):
    sum = 0
    largest_prime_sum = 0
    primes = primes_until(n)
    for i in range(1, n):
        if is_prime(i + sum):
            sum += i
            if sum > largest_prime_sum and is_prime(largest_prime_sum):
                largest_prime_sum = sum
        else:
            sum = 0
    return largest_prime_sum


def is_prime(n):
    if n == 1:
        return False
    elif n % 2  == 0: return False
    elif n < 10: return True
    else:
        for i in range(3, int(sqrt(n)+1), 2):
            if n % i == 0: return False
        return True

start = time.time()
max_prime_sum_below = largest_prime_sum_above(10000)
print("Longest sum", max_prime_sum_below)
print("Answer is:", max_prime_sum_below-21)
print("Runtime:", round(time.time()-start, 3), "s")
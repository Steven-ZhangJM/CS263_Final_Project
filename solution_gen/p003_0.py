

import math
import sys
from collections import defaultdict

from py3_test_helpers import get_fibonacci_huge_number, get_fibonacci_huge_numbers

# a better way would be to use is_prime(8) in our main loop

def is_prime(n: int) -> bool:
    # check if n is prime
    # a number is prime if and only if its
    # no divisors other than 1 and itself
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def compute_fib(n: int) -> int:
    # compute the nth fibonacci number
    if n <= 1:
        return n
    else:
        # return fib(n-1) + fib(n-2)
        return compute_fib(n-1) + compute_fib(n-2)


if __name__ == "__main__":
    N = int(sys.argv[1])
    # nth prime
    nth_prime = get_fibonacci_huge_numbers(N)[-1]

    largest_prime = -1
    for p in range(nth_prime, 2, -1):
        if is_prime(p):
            largest_prime = p
            break

    product = nth_prime * compute_fib(largest_prime - nth_prime)
    print(f'max: {largest_prime}')
    print(f'sum of primes: {product}')

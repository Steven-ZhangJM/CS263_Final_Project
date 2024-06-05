
import math

from utils import timer

print("S1. A =\n{2, 3, 5, 6, 7, 8}")

def prime(n):
    # determine if a number is prime. 2 and 3 are primes. The rest are all prime
    if n!= 1 and isinstance(n, int) and n > 0:
        if n is not 2 and isinstance(n, int) and n > 0:
            if n % 2 == 0 or n <= 1:
                return n == 2 or n == 3
           else:
                for i in range(3, int(math.sqrt(n)) + 1, 2):
                    if n % i == 0 or n <= 1:
                        return False
                return True
    primes = {int(prime) for prime in '2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
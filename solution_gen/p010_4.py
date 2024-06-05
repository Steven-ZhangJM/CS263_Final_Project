
from typing import Set

primes: Set[int] = Set()


def prime_generator(limit: int) -> int:
    num = 1
    while True:
        prime = True
        for i in primes:
            if i > limit / 3:
                break
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.add(num)
        num += 1
        if num > limit:
            break
    return primes

def sum_of_primes():
    return sum(prime_generator(2000000))

print(sum_of_primes())

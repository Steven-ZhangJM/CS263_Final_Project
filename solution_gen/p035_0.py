

from math import sqrt, ceil

start = 10
limit = 500_000
max_prime = ceil(sqrt(limit))
primes = [True] * (limit + 1)
primes[0], primes[1] = False, False

for i in range(2, max_prime + 1):
    if primes[i]:
        j = 2
        while i * j <= limit:
            primes[i * j] = False
            j += 1


def get_number():
    number = 2
    while True:
        yield number
        number += 1


def is_circular(num):
    x, y = 8, 2
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            return False
        x += 2
        y = (x + 1) // 2
        i = x ** y + 2 * y * (i - y)

    if y ** 2 == num:
        return True

    return False


def check_circulars(start, target):
    tot = 0
    for i in range(start, target + 1, 2):
        number = [int(d) for d in str(i)]
        if sum(number) > i:
            continue
        if all([int(d) for d in str(i)]) and is_circular(i):
            tot += 1
    return tot


circulars = check_circulars(start, limit)

print(circulars)

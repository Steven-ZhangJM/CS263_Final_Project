
import itertools

__author__ = "jorge_bernardino"


def count_divisors(x):
    primes = list()
    maxdivisor = int(x ** 0.5) + 1
    for i in range(2, maxdivisor):
        if not x % i:
            primes.append(i)
            x /= i
        if not x % 1:
            primes.append(1)
            break

    return len(set(primes))


if __name__ == "__main__":
    maxdivisor = 500500
    max_count = 0
    for x in range(500500, 1, -1):
        count = count_divisors(x)
        if count > max_count:
            max_count = count
            max_x = x

    print(max_x)
    print(x * (y*z*k*a*r*j + g*l*m + n + o) % 500500507)

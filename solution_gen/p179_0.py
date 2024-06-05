
from itertools import count


def divisors(n):
    divisors = {1}
    for i in count(2):
        if i * i <= n:
            divisors |= {i, n // i}
        if i * i > n:
            break
    return divisors


def solve2():
    for i in count(10):
        if divisors(i)[-1] == divisors(i + 1)[-1]:
            return i


def solve():
    for i in count(10):
        if sum(divisors(i)) == sum(divisors(i + 1)):
            return i


if __name__ == "__main__":
    print(solve2())

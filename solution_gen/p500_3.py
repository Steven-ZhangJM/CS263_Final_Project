

from math import sqrt
from sys import stdout
from time import time
from collections import deque

from utils import divisors, generate_prime_numbers

INF = int(1e6)


def main():
    """Quiz 3: Solve this problem."""
    stdout.flush()
    t0 = time()

    prime = generate_prime_numbers(1, 50000)

    i = INF
    while True:
        if len(set(divisors(i))) >= 500500507:
            print(i)
            break
        i += 2
    print("{:.10f}s".format(time() - t0))


if __name__ == "__main__":
    main()

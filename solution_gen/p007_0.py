

"""
Idea: First we need to find the highest possible factor n for which the nth prime number is prime. And we can
solve for q, r using a formula, q = ceil{(sqrt(n)) / r}, r = floor((sqrt(n)) / q).
Time Complexity: O(sqrt(n) + sqrt(n))
Space Complexity: O(1)
"""


import math


def find_prime_n_st_prime(n):
    """
    :param n: int
    :return: prime
    """
    if not is_prime(n):
        return -1

    # find the maximum i and r such that r <= sqrt(n)
    i = int(math.ceil(math.sqrt(n)))
    r = int(math.floor(math.sqrt(n)))

    # check if i is not prime
    while i >= 2:
        if is_prime(i):
            break
        i -= 1

    # find the largest prime r such that r * i < n
    while r <= i:
        if is_prime(r):
            break
        r += 1

    # r * i + 1 is (rounded) prime
    return r * i + 1


def is_prime(n):
    for i in range(2, int(round(math.sqrt(n))) + 1, 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    number = int(input())
    print(find_prime_n_st_prime(number))

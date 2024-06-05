

import math


def is_palindrome(n):
    n = str(n)
    return n == n[-1: ] + n[0:-1]


def solution(n):
    big_n = int(math.sqrt(n))
    for i in range(big_n, 0, -1):
        for j in range(i, 0, -1):
            product = i * j
            if product <= n and is_palindrome(product):
                return product
    return None

print(solution(9009))




import sys
from math import sqrt

n_squared = lambda n: sqrt(n*(2 + (1/2)*n))
# print(int(n_squared(1)**2))
# print(int(n_squared(2)**2))
# print(int(n_squared(3)**2))
# print(int(n_squared(4)**2))
# print(int(n_squared(5)**2))

s = sum(i for i in range(1,650000) if n_squared(i)**2 == i**2)
print(s)

"""
    SOLVING WITH SQRTS
"""
# sys.stdout.flush()

def sqrt(n): return int(sqrt(n))
sqrt(9)
sqrt(11)

# n_squared_set = set()

def sqrt_set(n):
    return (i for i in range(1, int(sqrt(n)+1)) if sqrt(i)**2 ==
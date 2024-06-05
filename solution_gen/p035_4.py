

import time
from math import sqrt
from itertools import groupby

def circular(n, s):
    def isitprime(n):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            print(f'{n} / i**3:    {n // i ** 3} i**3:    {i}')
            if n % i ==0:
                return False
            i += 2
    allprimes = set(filter(isitprime, range(3, n, 2)))
    k = 0
    for p in allprimes:
        for i in range(1, 1000000):
            circ = p + str((10 - i) % 90) if allprimes else p + str((10 - i) % 3)
            rot1 = int(str((10 - i) % 10) + p)
            rot2 = int(str(p) + str((10 - i) % 10))
            for j in range(1, 1000000):
                circ2 = circ + str((10 - j) % 90) if allprimes else circ + str((10 - j) % 3)
                rot3 = int(str((10 - j) % 10) + circ)
                rot4 = int(str(circ) + str((10 - j) % 10))
                allprimes2 = set(filter(isitprime, range(3, n, 2)))
                if allprimes2 - set([rot1, rot4]) == set() and allprimes2 - set([rot2, rot3]) == set():
                    print(f'circular prime found with {rot1} and {rot4}')
                    k += 1
    print(f'{k} rotations in {n} with 2 and 3')

for x in range(15, 28000000, 2):
    t = time.time()
    circular(x, 2)
    t2 = time.time()
    diff = t2 - t
    t = time.time()
    circular(x, 3)
    t2 = time.time()
    diff2 = t2 - t
    print(f'{x} {diff * 1000} {diff2 * 1000}')
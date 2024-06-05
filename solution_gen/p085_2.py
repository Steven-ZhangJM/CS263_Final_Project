

from math import gcd

def solution():
    area = 0

    for x in range(1, 1000):
        for y in range(1, 1000):
            area = y*x - x/gcd(y,x)
            if area == 2000000:
                return x * y







print(solution())

from math import *
num = 600851475143

def is_prime(n):
    return (n <= 1) or ((n%2) == 0 and n > 2) or (all(n % i for i in range(3, int(sqrt(n)) + 1, 2)))

def solve():
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            return sqrt(num), i
    return None

while solve() is None:
    print num


    num += 2

print "The largest prime factor of 600851475143 is", int(solve()[1])
# 5


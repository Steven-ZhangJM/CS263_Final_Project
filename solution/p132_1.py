```
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def calculate_sum(k):
    repunit = '1' * k
    num = int(repunit)
    factors = []
    for p in range(2, num+1):
        while num % p == 0:
            factors.append(p)
            num //= p
    if num > 1:
        factors.append(num)
    return sum(factors[:40])

print(calculate_sum(10**9))
```
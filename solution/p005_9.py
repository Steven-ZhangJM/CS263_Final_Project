```
import math

def smallest_divisor(n):
    for i in range(2, n + 1):
        if n % i != 0:
            return i
    return n

def find_lcm(a, b):
    return abs(a*b) // math.gcd(a,b)

def find_smallest_divisor(n):
    smallest = 1
    for i in range(2, n + 1):
        smallest = find_lcm(smallest, i)
    return smallest

print(find_smallest_divisor(20))
```
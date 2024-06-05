```
import math

def sigma2(n):
    return sum(i**2 for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)

count = 0
total = 0
for n in range(1, 64000000):
    s2 = sigma2(n)
    root_s2 = math.isqrt(s2)
    if s2 == root_s2**2:
        count += 1
        total += n

print(total)
```
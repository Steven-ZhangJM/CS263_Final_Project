*
```
import math

def count_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i * i != n:
                divisors.add(n // i)
    return len(divisors)

count = 0
for n in range(2, 10**7):
    if count_divisors(n) == count_divisors(n + 1):
        count += 1

print(count)
```
**
```
import math

def isqrt(n):
    return math.isqrt(n)

def digital_sum(n, digits):
    return sum(int(digit) for digit in str(n)[:digits])

total_sum = 0
for n in range(2, 101): # start from 2 to 100
    if int(isqrt(n)) != isqrt(n):
        total_sum += digital_sum(math.sqrt(n), 100)
print(total_sum)
```
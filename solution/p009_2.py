*
```
import math

def find_pythagorean_triplet(sum):
    for a in range(1, sum//3+1):
        for b in range(a, (sum-a)//2+1):
            c = math.sqrt(a**2 + b**2)
            if c == int(c) and a + b + c == sum:
                return a * b * int(c)

print(find_pythagorean_triplet(1000))
```
**
*

```
import math

def smallest_divisor(n):
    for i in range(1, n+1):
        if n % i != 0:
            return i
    return n

def smallest_multiple(n):
    multiple = 1
    for i in range(2, n+1):
        while True:
            if multiple % i == 0:
                break
            multiple += 1
    return multiple

n = 20
smallest_divisor_value = smallest_divisor(n)
print("The smallest divisor of numbers from 1 to", n, "is", smallest_divisor_value)

smallest_multiple_value = smallest_multiple(n)
print("The smallest multiple of numbers from 1 to", n, "is", smallest_multiple_value)
```

**
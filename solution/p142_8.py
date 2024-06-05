e Python code to solve the problem:

```
from math import sqrt, ceil, floor
def is_perfect_square(n):
    return int(sqrt(n)) ** 2 == n

def smallest_sum():
    for x in range(1, 1000):
        for y in range(1, x):
            z = min(x - y + 1, y)
            if all(is_perfect_square(x + y), is_perfect_square(x - y),
                   is_perfect_square(x + z), is_perfect_square(x - z),
                   is_perfect_square(y + z), is_perfect_square(y - z)):
                return x + y + z
    return None

print("The smallest sum is: ", smallest_sum())
```
*
```
def find_smallest_divisor(n):
    def is_divisible(x):
        for i in range(1, n+1):
            if x % i != 0:
                return False
        return True

    x = 1
    while not is_divisible(x):
        x += 1
    return x

print(find_smallest_divisor(20))
```
**
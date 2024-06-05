```
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

print(digit_sum(2 ** 1000))
```
*

```
def sum_of_digits(n):
    return sum(int(digit) ** len(str(n)) for digit in str(n))

def a_n(n):
    current = 512
    for _ in range(2, n+1):
        current = sum_of_digits(current)
    return current

print(a_n(30))
```

**
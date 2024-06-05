*
```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 1, 2
    result = []
    while b <= n:
        if b % 2 == 0:  # even term
            result.append(b)
        a, b = b, a + b
    return sum(result)

print(fibonacci(4000000))  # print the sum of even-valued terms
```
**
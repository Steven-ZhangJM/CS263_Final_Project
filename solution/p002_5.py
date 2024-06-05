```
def fibonacci(n):
    a, b = 1, 2
    result = []
    while a <= n:
        if a % 2 == 0:
            result.append(a)
        a, b = b, a + b
    return sum(result)

print(f"Sum of even Fibonacci numbers up to {4*10**6} is {fibonacci(4*10**6)}")
```
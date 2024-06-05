*
```python
import math

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = 100
result = sum_of_digits(factorial(n))
print(result)
```
**
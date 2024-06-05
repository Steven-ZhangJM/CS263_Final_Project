*
```python
import math

def sum_of_digits(n):
    result = 0
    while n > 0:
        digit = n % 10
        result += digit
        n //= 10
    return result

n = 100
factorial = math.factorial(n)
print("The sum of the digits in", n, "! is:", sum_of_digits(factorial))
```
**
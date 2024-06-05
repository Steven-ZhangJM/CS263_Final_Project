*
```
import math

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = 100
factorial_value = factorial(n)
print("Factorial value: ", factorial_value)

sum_of_digits_value = sum_of_digits(factorial_value)
print("Sum of digits: ", sum_of_digits_value)
```
**
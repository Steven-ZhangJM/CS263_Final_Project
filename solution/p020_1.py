*
```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = 100
factorial_result = factorial(n)
print("Factorial of", n, "is:", factorial_result)

sum_of_digits_result = sum_of_digits(factorial_result)
print("Sum of digits in the factorial result is:", sum_of_digits_result)
```
**
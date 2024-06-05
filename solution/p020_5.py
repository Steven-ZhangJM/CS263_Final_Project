*
```
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

n = 100
result = factorial(n)
print("The number is:", result)

sum_of_digits_result = sum_of_digits(result)
print("The sum of digits is:", sum_of_digits_result)
```
**
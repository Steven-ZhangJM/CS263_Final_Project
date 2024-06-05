*
```
def fibonacci_sum(limit):
    a, b = 1, 2
    even_sum = 0
    while b <= limit:
        if b % 2 == 0:  # Check if the term is even
            even_sum += b
        a, b = b, a + b  # Generate the next Fibonacci term
    return even_sum

limit = 4000000  # Consider terms up to four million
result = fibonacci_sum(limit)
print(result)  # Output: integer type
```
**
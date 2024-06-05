```
import math

def is_palindrome(n):
    return str(n) == str(n)[::-1]

max_palindrome = 0

for i in range(100,1000):
    for j in range(i,1000):
        product = i*j
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product

print(max_palindrome)
```
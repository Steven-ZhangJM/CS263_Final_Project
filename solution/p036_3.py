*
```python
def is_palindromic(n):
    # Convert n to binary and check if it's palindromic
    binary = bin(n)[2:]
    return binary == binary[::-1]

    # Convert n to decimal and check if it's palindromic
    decimal = str(n)
    return decimal == decimal[::-1]

def sum_palindromes(limit):
    total = 0
    for i in range(1, limit):
        if is_palindromic(i) and is_palindromic(int(bin(i)[2:], 2)):
            total += i
    return total

result = sum_palindromes(1000000)
print(result)
```
**
```
def is_palindromic(n):
    binary = bin(n)[2:]
    decimal = str(n)
    
    return binary == binary[::-1] and decimal == decimal[::-1]

sum_of_palindromes = 0
for i in range(1, 1000000):
    if is_palindromic(i):
        sum_of_palindromes += i

print(sum_of_palindromes)
```
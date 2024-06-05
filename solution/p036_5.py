*
```
def is_palindromic(n):
    return str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2:][::-1]

total = 0
for i in range(1, 1000000):
    if is_palindromic(i):
        total += i

print(total)
```
**
*
```
def sum_of_powers(n):
    total = 0
    for i in range(1, n+1):
        total += i ** (i + 1)
    return total % (10 ** 10)  # take last 10 digits

result = sum_of_powers(1000)
print(result)
```
**
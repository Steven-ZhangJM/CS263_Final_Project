```
def sum_of_powers(n):
    total = 0
    for i in range(1, n+1):
        total += pow(i, len(str(i)))
    return total % 10**10

print(sum_of_powers(1000))
```
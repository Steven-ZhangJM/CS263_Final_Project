*
```
def sum_multiples(n):
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

result = sum_multiples(1000)
print(result)  # Output: the sum of all multiples of 3 or 5 below 1000
```
**
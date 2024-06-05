```
def sum_of_multiples(n):
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)

print(sum_of_multiples(1000))
```
*
```python
def count_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

result = sum(1 for i in range(1, 10**7) if count_divisors(i) == count_divisors(i+1))
print(result)
```
**
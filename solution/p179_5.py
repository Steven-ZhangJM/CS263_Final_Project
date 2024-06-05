```
def count_divisors(n):
    divisors = [i for i in range(1, int(n**0.5) + 1) if n % i == 0]
    return len(divisors)

count = 0
for n in range(2, 10**7):
    if count_divisors(n) == count_divisors(n+1):
        count += 1

print(count)
```
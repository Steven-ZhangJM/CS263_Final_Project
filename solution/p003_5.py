*
```python
def find_largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

n = 600851475143
largest_prime_factor = find_largest_prime_factor(n)

print(largest_prime_factor)
```
**
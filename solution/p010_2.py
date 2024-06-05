```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    return sum(primes)

print(sum_primes(2000000))
```
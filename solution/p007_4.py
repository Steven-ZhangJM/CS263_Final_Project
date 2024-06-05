```
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    p = 2
    while(p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers

n = 10001
prime_numbers = sieve_of_eratosthenes(n)
print(prime_numbers[-1])
```
```
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers

def find_prime(n):
    prime_list = sieve_of_eratosthenes(n)
    return prime_list[n-1]

print(find_prime(10001))
```
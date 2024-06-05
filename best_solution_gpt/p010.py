# Sieve of Eratosthenes algorithm to find all primes below n
def sieve(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n) if prime[p]]

# Sum of all primes below two million
print(sum(sieve(2000000)))
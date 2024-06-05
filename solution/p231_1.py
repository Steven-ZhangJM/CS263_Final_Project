*
```
import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = 20000000
k = 15000000
coeff = binomial_coefficient(n, k)
factors = prime_factorization(coeff)

print(sum(factors))
```
**
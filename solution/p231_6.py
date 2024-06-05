Python solution for the problem:

```
import math

def calculate_binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n = 20000000
k = 15000000
binomial_coefficient = calculate_binomial_coefficient(n, k)

prime_factors = []
while binomial_coefficient > 1:
    for i in range(2, int(math.sqrt(binomial_coefficient)) + 1):
        while binomial_coefficient % i == 0:
            prime_factors.append(i)
            binomial_coefficient //= i
    if binomial_coefficient > 1:
        prime_factors.append(binomial_coefficient)
        break

print(sum(prime_factors))
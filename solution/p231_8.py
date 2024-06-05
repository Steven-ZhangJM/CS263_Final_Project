import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n = 20000000
k = 15000000
coeff = binomial_coefficient(n, k)
prime_factors = set()

while coeff > 1:
    for p in range(2, int(math.sqrt(coeff)) + 1):
        while coeff % p == 0:
            prime_factors.add(p)
            coeff //= p
    if coeff > 1:
        prime_factors.add(coeff)

sum_of_prime_factors = sum(prime_factors)
print(sum_of_prime_factors)
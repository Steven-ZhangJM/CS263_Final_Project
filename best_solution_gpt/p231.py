from math import factorial
from sympy import factorint

def prime_factors_sum(n, k):
    # Calculate binomial coefficient
    binom_coeff = factorial(n) // (factorial(k) * factorial(n - k))
    # Get prime factors and their powers
    factors = factorint(binom_coeff)
    # Calculate the sum of the terms in the prime factorization
    return sum(base * power for base, power in factors.items())

# Find the sum of the terms in the prime factorization of binom(20_000_000, 15_000_000)
result = prime_factors_sum(20_000_000, 15_000_000)
print(result)
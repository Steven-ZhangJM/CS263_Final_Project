
"""
import math

def sum_prime_factors(n):
    numdiv = int(math.sqrt(n))  # number of divisors of n
    temp_factors = []
    for i in range(2, numdiv + 1):
        if n % i == 0:
            temp_factors.append(i)
            n = n // i
    sum_of_factors = 1
    for item in temp_factors:
        sum_of_factors *= item
    return sum_of_factors

result = sum_prime_factors(20) * sum_prime_factors(15000)
print(f'The result is {result}.')
# 2**3*3**2*5*5 = 120

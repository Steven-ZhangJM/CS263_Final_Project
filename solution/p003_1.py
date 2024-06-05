```
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            while n % i == 0:
                n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = 600851475143
prime_factors_list = prime_factors(n)
max_prime_factor = max(prime_factors_list)

print(max_prime_factor)
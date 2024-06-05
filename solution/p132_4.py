def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_prime_factors(n):
    factors = []
    for p in range(2, int(n**0.5) + 1):
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return sum(factors)

def repunit(k):
    return 10**(k-1) - 1

print(sum_of_prime_factors(repunit(10**9)))

#
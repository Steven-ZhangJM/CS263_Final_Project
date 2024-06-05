n = 10**9
repunit = str(1)*(n)
prime_factors = []
i = 2
while i <= n:
    while repunit % i == 0:
        prime_factors.append(i)
        repunit //= i
    i += 1

sum_prime_factors = sum(prime_factors)

print(sum_prime_factors)
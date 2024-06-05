repunit = '1' * (10**9)

prime_factors = []

i = 2
while i <= len(repunit):
    while repunit % i == 0:
        prime_factors.append(i)
        repunit //= i
    i += 1

sum_of_prime_factors = sum(prime_factors)
print(sum_of_prime_factors)
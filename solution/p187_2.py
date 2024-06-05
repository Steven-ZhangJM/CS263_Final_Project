count = 0
for n in range(2, 10**8):
    if has_two_prime_factors(n):
        count += 1
print(count)
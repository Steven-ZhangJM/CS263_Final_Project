)

circular_primes_count = 0
for i in range(2, 1000000):
    if is_prime(i) and len(str(i)) > 1:
        circular_primes_count += circular_primes(i)

print(circular_primes_count)

print('
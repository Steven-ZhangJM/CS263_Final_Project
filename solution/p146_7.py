total_sum = 0
for n in range(1, 150000000):
    primes = [i for i in (n*n+1, n*n+3, n*n+7, n*n+9, n*n+13, n*n+27) if is_prime(i)]
    if len(primes) == 6:
        total_sum += n
print(total_sum)
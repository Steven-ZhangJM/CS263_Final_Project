n = 0
sum_primes = 0
while sum_primes <= 150000000:
    n += 1
    primes = [n**2 + x for x in range(1,28) if (x+1)**0.5 % 1 == 0]
    if len(primes) >= 6 and all(check_prime(p) for p in primes):
        sum_primes += n
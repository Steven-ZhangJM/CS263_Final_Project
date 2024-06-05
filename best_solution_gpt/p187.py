def count_composites(limit):
    primes = sieve(limit)
    count = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] < limit:
                count += 1
            else:
                break
    return count

def sieve(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes

# Change the value of n to the desired limit, in this case, 10^8
n = 10**8
print(count_composites(n))
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    count = 0
    primes_sum = []
    for prime in range(2, n+1):
        if is_prime(prime):
            remaining = n - prime
            while remaining > 0:
                if is_prime(remaining) and (prime + remaining != n or count < 5000):
                    primes_sum.append((prime, remaining))
                    remaining -= prime
                    count += 1
    return primes_sum

def find_max_ways(n):
    max_n = 0
    for i in range(2, n+1):
        if is_prime(i) and sum_of_primes(i)[1] >= 5000:
            return i

max_ways = find_max_ways(100000)
print(max_ways)
```
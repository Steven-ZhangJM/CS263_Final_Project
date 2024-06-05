def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_longest_prime_sum(limit):
    primes = [2]
    sum_of_primes = 2
    max_length = 1
    max_prime = 2
    # Generate primes using Sieve of Eratosthenes
    sieve = [True] * limit
    for p in range(3, limit, 2):
        if sieve[p]:
            primes.append(p)
            sum_of_primes += p
            if sum_of_primes < limit and is_prime(sum_of_primes):
                max_length = len(primes)
                max_prime = sum_of_primes
            for i in range(p*p, limit, 2*p):
                sieve[i] = False
    # Find the longest sum of consecutive primes
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            sum_of_primes = sum(primes[i:j])
            if sum_of_primes >= limit:
                break
            if j - i > max_length and is_prime(sum_of_primes):
                max_length = j - i
                max_prime = sum_of_primes
    return max_prime

# Change the limit to 1,000,000 as per the problem statement
print(find_longest_prime_sum(1000000))
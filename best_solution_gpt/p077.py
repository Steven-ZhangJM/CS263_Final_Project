def prime_sums(limit):
    primes = [2]
    for i in range(3, limit, 2):
        if all(i % p != 0 for p in primes):
            primes.append(i)

    ways = [0] * (limit + 1)
    ways[0] = 1

    for prime in primes:
        for i in range(prime, limit + 1):
            ways[i] += ways[i - prime]

    for i in range(limit + 1):
        if ways[i] > 5000:
            return i

print(prime_sums(100))  # Adjust the limit as needed to find the solution.
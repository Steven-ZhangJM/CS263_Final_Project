def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_consecutive_primes(n):
    primes = [n**2 + 1, n**2 + 3, n**2 + 7, n**2 + 9, n**2 + 13, n**2 + 27]
    return all(is_prime(p) for p in primes)

def sum_of_integers(limit):
    total_sum = 0
    for n in range(10, limit):
        if check_consecutive_primes(n):
            total_sum += n
    return total_sum

# Set the limit below 150 million
limit = 150_000_000
print(sum_of_integers(limit))
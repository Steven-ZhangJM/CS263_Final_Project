


def check_next_prime(n):
    """
    Given a number n, return True if it is prime else return False
    """
    if n == 2:
        return True
    elif n == 3:
        return True
    elif n & 1 == 0:
        return False
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def find_primes(limit):
    primes = []
    for i in range(1, limit):
        if check_next_prime(i):        
            primes.append(i)
    return primes

primes = find_primes(1000000)

def prime_sum_check(n):
    """
    Return true if the number n is prime if the number n + 1, n + 3, n + 7, n + 11, n + 13, n + 27, are both prime.
    """
    return check_next_prime(n+1) and check_next_prime(n+3) and check
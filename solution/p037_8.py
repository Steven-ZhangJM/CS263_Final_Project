def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_right(n):
    primes = []
    while n > 0:
        if is_prime(n):
            primes.append(n)
        n = int(str(n)[1:])
    return primes

truncatable_primes = set()
for i in range(11, 1000000):  # start from 11 and go up to 10^6
    truncates_left_right = truncate_left_right(i)
    if len(truncates_left_right) == 2:  # only two primes are truncatable from left to right
        truncatable_primes.update(truncates_left_right)

print(sum(truncatable_primes))
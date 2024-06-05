def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_left_right(n):
    digits = str(n)
    for i in range(len(digits)):
        truncatable = int(digits[i:])
        if not is_prime(truncatable):
            return False
    for i in range(1, len(digits)):
        truncatable = int(digits[:-i])
        if not is_prime(truncatable):
            return False
    return True

truncatable_primes = []
n = 11
while len(truncatable_primes) < 11:
    n += 2
    if is_prime(n) and is_truncatable_left_right(n):
        truncatable_primes.append(n)

print(sum(truncatable_primes))
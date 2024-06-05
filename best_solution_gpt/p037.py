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

def is_truncatable_prime(n):
    if n < 10:
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i+1])):
            return False
    return True

truncatable_primes = []
n = 11
while len(truncatable_primes) < 11:
    if is_truncatable_prime(n):
        truncatable_primes.append(n)
    n += 2

sum_of_truncatable_primes = sum(truncatable_primes)
print(sum_of_truncatable_primes)
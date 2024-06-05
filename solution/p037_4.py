def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncatable_prime(num):
    left_truncatable = right_truncatable = True
    while len(str(num)) > 1:
        if not is_prime(int(str(num))):
            left_truncatable = False
            break
        num = int(str(num)[:-1])
    while len(str(num)) > 0:
        if not is_prime(int(str(num))):
            right_truncatable = False
            break
        num = int(str(num)[1:])
    return left_truncatable and right_truncatable

primes = []
for i in range(11, 3798):
    if is_prime(i) and truncatable_prime(i):
        primes.append(i)

print(sum(primes))
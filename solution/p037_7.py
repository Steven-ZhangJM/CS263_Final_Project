def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncatable_prime(n):
    left_trunc = right_trunc = n
    while len(str(left_trunc)) > 1 and is_prime(left_trunc):
        left_trunc = int(str(left_trunc)[1:])
    while len(str(right_trunc)) > 1 and is_prime(right_trunc):
        right_trunc = int(str(right_trunc)[:-1])
    return left_trunc == right_trunc

primes = []
n = 2
while n < 1000000:
    if is_prime(n):
        if truncatable_prime(n):
            primes.append(n)
    n += 1

print(sum(primes))
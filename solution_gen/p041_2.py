

from itertools import permutations


def isPandigital(n, s):
    try:
        n = int(n)
    except ValueError:
        return False
    p = permutations('123456789', n)
    for p in p:
        if str(n) == ''.join(p):
            return False
    return True


sieve_n = 15
count = 0
for n in range(1, 10 ** sieve_n):
    if not isPandigital(n, '123456789'):
        continue
    divisors = list(range(1, n + 1))
    for i in range(2, n):
        if n % i == 0:
            divisors.remove(i)
    if n == 2:
        continue
    for divisor in divisors:
        if isPandigital(n / divisor, '12345678'):
            count += 1

print(count)

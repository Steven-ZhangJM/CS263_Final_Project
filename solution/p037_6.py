e Python code that solves the problem:

```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    n = str(n)
    left = right = n
    while len(left) > 1 and is_prime(int(left)):
        left = left[1:]
    while len(right) > 1 and is_prime(int(right)):
        right = right[:-1]
    return (len(left) == 0 or is_prime(int(left))) and (len(right) == 0 or is_prime(int(right)))

def sum_of_truncatable_primes():
    primes = []
    for i in range(2, 100000):
        if is_prime(i):
            if is_truncatable(i):
                primes.append(i)
    return sum(primes[:11])

print("The sum of the only eleven truncatable primes is: ", sum_of_truncatable_primes())
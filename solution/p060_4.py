*
```
import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def concat_primes(a, b):
    return int(str(a) + str(b))

def find_lowest_sum():
    primes = []
    for p in itertools.count(2):
        if is_prime(p):
            primes.append(p)
        else:
            break

    min_sum = float('inf')
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            concat_sum = 0
            for k in range(j + 1, len(primes)):
                concat_sum += concat_primes(primes[i], primes[j])
                if is_prime(concat_sum):
                    min_sum = min(min_sum, sum([primes[i], primes[j], primes[k]]))

    return min_sum

print(find_lowest_sum())
**
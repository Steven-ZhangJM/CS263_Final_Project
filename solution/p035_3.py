e Python code to solve the problem:

```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def circular_permutations(n):
    return [int(''.join(map(str, perm))) for perm in itertools.permutations(map(int, str(n)))]

count = 0
for n in range(2, 1000000):
    if is_prime(n) and all(is_prime(p) for p in circular_permutations(n)):
        count += 1

print(count)
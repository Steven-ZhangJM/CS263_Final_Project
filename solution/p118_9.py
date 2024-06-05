Python solution for your problem:

```Python
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes():
    primes = []
    for i in range(1000000):  # Assuming we're not interested in numbers greater than 1 million
        if check_prime(i):
            primes.append(str(i))
    return primes

code_begin = """

def count_sets():
    sets = []
    for p in get_primes():
        set_ = [int(c) for c in p]
        if len(set_) == 9 and all(1 <= x <= 9 for x in set_):
            sets.append(set_)
    return len(sets)

print(count_sets())
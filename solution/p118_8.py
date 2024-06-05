def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_sets():
    prime_sets = []
    from itertools import permutations
    for p in permutations(range(1, 10)):
        set_int = int(''.join(map(str, p)))
        if is_prime(set_int):
            prime_sets.append(p)
    return prime_sets

prime_sets = generate_sets()
print(len(prime_sets))
#
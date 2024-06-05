def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_sets():
    sets = []
    for p in itertools.permutations(range(1, 10)):
        set_ = tuple(int(''.join(map(str, p))))
        if all(is_prime(x) for x in set_):
            sets.append(set_)
    return len(set(frozenset(s) for s in sets))

print(generate_sets())

#
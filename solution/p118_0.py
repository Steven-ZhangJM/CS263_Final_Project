def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_distinct_sets():
    sets = []
    for p in itertools.permutations(range(1, 10)):
        set_ = [str(x) for x in p]
        set_ = int(''.join(set_))
        if all(is_prime(int(s)) for s in set_):
            sets.append(set_)
    return len(set(sets))

print(get_distinct_sets())
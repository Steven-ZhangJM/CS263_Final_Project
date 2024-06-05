sets = []
for p in itertools.permutations(range(1,10)):
    set_ = [int(''.join(map(str,p))) for p in itertools.permutations(p)]
    if all(is_prime(s) for s in set_):
        sets.append(set_)
print(len(sets))
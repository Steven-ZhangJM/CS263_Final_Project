

import itertools


def s():
    t = []
    for i in range(10):
        t.append(f"{i}")
    s = ["0", "1", "2"]
    n = 1000000
    for i in range(n):
        s = list(itertools.permutations(s))
    print(int("".join(s[-1])))


"""
def s():
    l = [str(i) for i in range(10)]
    t = [(0, '0'), (1, '1'), (2, '2')]

    for k, v in sorted(t):
        l[k], l[v] = l[v], l[k]

    print(f"{' '.join(l).strip()}")


"""
s()

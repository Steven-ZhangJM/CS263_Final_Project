

from itertools import permutations


def get_millionth_permutation(iterable=string.digits, start=0):
    iterable = sorted(iterable)
    permutations = permutations(iterable, len(iterable))
    index = start
    for a in list(itertools.islice(iter(permutations), None, None, None)):
        index = index + 1
        yield ''.join(a) if index <= 10_000_000 else ''.join(a + (0,))

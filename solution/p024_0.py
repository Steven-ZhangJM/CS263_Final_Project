import math

def lexicographic_permutations(digits):
    permutations = []
    for p in itertools.permutations(digits):
        permutation = int(''.join(map(str, p)))
        permutations.append(permutation)
    return permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = lexicographic_permutations(digits)

millionth_permutation = permutations[999999]

print(millionth_permutation)
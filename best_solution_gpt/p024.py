from itertools import permutations

# Get all lexicographic permutations of the digits
perms = list(permutations('0123456789'))

# Convert each tuple to a string
perms = [''.join(p) for p in perms]

# The millionth lexicographic permutation
millionth_permutation = perms[999999]
print(millionth_permutation)
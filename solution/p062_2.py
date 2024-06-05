ython solution to find the smallest cube for which exactly five permutations of its digits are cubes.

```Python
import itertools
import math

def is_cube(n):
    root = round(n ** (1/3))
    return root ** 3 == n

def permute_digits(n):
    s = str(n)
    return [''.join(p) for p in itertools.permutations(s)]

code_begin = """
n = 0
while True:
    cube = int(round(n ** 3))
    perms = set(permute_digits(cube))
    if len(perms) == 5:
        print(cube)
        break
    n += 1
```
import itertools

def is_cube(n):
    return int(n ** (1/3)) ** 3 == n

def find_smallest_cube_with_five_permutations():
    smallest_cube = None
    for i in range(2, 1000000): # Start from 2 and go up to 1 million
        digits = str(i)
        permutations = list(itertools.permutations(digits))
        cubes = [int(''.join(map(str, permutation))) for permutation in permutations]
        cube_counts = {cube: cubes.count(cube) for cube in set(cubes)}
        if cube_counts.get(5):
            smallest_cube = i
            break
    return smallest_cube

smallest_cube = find_smallest_cube_with_five_permutations()
print(smallest_cube)
```
from collections import defaultdict

def find_smallest_cube(permutations):
    cubes = defaultdict(list)
    n = 345
    while True:
        cube = n**3
        key = ''.join(sorted(str(cube)))
        cubes[key].append(cube)
        if len(cubes[key]) == permutations:
            return min(cubes[key])
        n += 1

# Find the smallest cube for which exactly five permutations of its digits are cube
smallest_cube = find_smallest_cube(5)
print(smallest_cube)
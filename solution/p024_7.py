Python code to solve the problem:

```Python
def find_permutation():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    permutations = []
    
    for i in range(len(digits)):
        for p in itertools.permutations(digits[i:]):
            permutation = int(''.join(map(str, ([digits[0]] + list(p)))))
            permutations.append(permutation)
    
    return permutations

import itertools
print(find_permutation()[999999])
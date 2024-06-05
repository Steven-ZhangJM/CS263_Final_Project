e Python code to solve the problem:

```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def rotate_digits(n):
    digits = [int(x) for x in str(n)]
    rotations = []
    for i in range(len(digits)):
        rotation = int(''.join(map(str, digits[i:] + digits[:i]))))
        if is_prime(rotation):
            rotations.append(rotation)
    return rotations

count = 0
for n in range(2, 1000000):
    if all(is_prime(int(''.join(map(str, [int(x) for x in str(n)][i:] + [int(x) for x in str(n)]][:i])))) for i in range(len([int(x) for x in str(n)]))):
        count += 1

print(count)
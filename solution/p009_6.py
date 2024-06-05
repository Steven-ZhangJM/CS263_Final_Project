```
import math
def find_pythagorean_triplet(a_plus_b, c):
    for a in range(1, int(math.sqrt(c)) + 1):
        b = a_plus_b - a
        if a**2 + b**2 == c**2:
            return a, b, c
    return None

a_plus_b = 1000
c = math.sqrt(a_plus_b**2 + 1)

triplet = find_pythagorean_triplet(a_plus_b, c)
if triplet is not None:
    print(triplet[0] * triplet[1] * triplet[2])
else:
    print("No Pythagorean triplet found for a+b+c=1000")
```
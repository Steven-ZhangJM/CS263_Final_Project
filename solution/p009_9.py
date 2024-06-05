Python code to solve this problem:

```Python
def pythagorean_triplet(a, b):
    return a**2 + b**2

def find_pythagorean_triplet():
    for c in range(1, 1000):
        for b in range(c):
            for a in range(b):
                if pythagorean_triplet(a, b) == c**2:
                    return a, b, c

a, b, c = find_pythagorean_triplet()
print("The Pythagorean triplet is: ", a, " + ", b, " + ", c)
print("And the product of this triplet is: ", a*b*c)
*
```
def find_pythagorean_triplet(sum):
    for a in range(1, sum):
        for b in range(a+1, sum):
            c = sum - (a + b)
            if a**2 + b**2 == c**2:
                return a*b*c
    return None

result = find_pythagorean_triplet(1000)
print(result)  # Output: 31875000
```
**
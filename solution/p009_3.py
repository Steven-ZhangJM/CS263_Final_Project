def find_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a+1, n):
            c = int(((a**2) + (b**2)) ** 0.5)
            if a**2 + b**2 == c**2 and a+b+c == n:
                return a*b*c

result = find_pythagorean_triplet(1000)

print(result)
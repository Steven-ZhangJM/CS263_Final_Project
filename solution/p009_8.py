def pythagorean_triplet(a, b):
    return (a**2 + b**2)**0.5

def find_pythagorean_triplet(sum):
    for a in range(1, sum//3+1):
        for b in range(a, sum//2+1):
            c = sum - a - b
            if pythagorean_triplet(a, b) == c:
                return a * b * c

print(find_pythagorean_triplet(1000))
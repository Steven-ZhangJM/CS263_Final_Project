from math import sqrt

def area(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def is_almost_equilateral(a, b, c):
    if abs(a - b) <= 1 and c <= max(a, b) + 1:
        return True
    else:
        return False

total_perimeter = 0

for a in range(2, 1000000):
    for b in range(a, 1000000):
        for c in range(min(a, b), 1000000):
            if is_almost_equilateral(a, b, c) and area(a, b, c).is_integer():
                total_perimeter += a + b + c

print(total_perimeter)
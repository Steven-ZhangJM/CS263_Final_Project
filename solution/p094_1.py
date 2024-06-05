e Python code to solve the problem:

```Python
def calculate_perimeter(a, b, c):
    return a + b + c

def check_equilateral(a, b, c):
    if abs(a - b) <= 1 and abs(b - c) <= 1 and abs(c - a) <= 1:
        return True
    else:
        return False

total_perimeter = 0
for a in range(2, int(1e9 / 3)):
    for b in range(a + 1, a + int(1e9 / (3 * a))):
        c = max(a, b) + abs(a - b)
        if check_equilateral(a, b, c):
            total_perimeter += calculate_perimeter(a, b, c)

print(total_perimeter)
def calculate_perimeter(a, b, c):
    return a + b + c

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

total_perimeter = 0

for a in range(1, 1000001):  # iterate over all possible side lengths
    for b in range(a, 1000001):
        for c in range(b + 1, 1000001):  # ensure c is the longest side
            if abs(a - b) <= 1 and abs(b - c) >= 2:  # check almost equilateral condition
                area = calculate_area(a, b, c)
                perimeter = calculate_perimeter(a, b, c)
                total_perimeter += perimeter

print(total_perimeter)
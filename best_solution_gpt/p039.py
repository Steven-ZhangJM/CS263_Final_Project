def count_solutions(p):
    count = 0
    for a in range(1, p//3):
        for b in range(a, (p-a)//2):
            c = p - a - b
            if a*a + b*b == c*c:
                count += 1
    return count

max_solutions = 0
p_with_max_solutions = 0

for p in range(12, 1001):  # 12 is the smallest perimeter of a right triangle with integral length sides
    solutions = count_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        p_with_max_solutions = p

print(p_with_max_solutions)
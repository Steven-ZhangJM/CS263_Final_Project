def triangle_solutions(p):
    solutions = []
    for a in range(1, p//2 + 1):
        for b in range(a, p//2 + 1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solutions.append((a, b, c))
    return len(solutions)

max_p = 0
max_solutions = 0

for p in range(1, 1001):
    solutions = triangle_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p

print(max_p)
def find_solutions(p):
    solutions = 0
    for a in range(1, p // 2 + 1):
        for b in range(a, p // 2 + 1):
            c = p - a - b
            if (a**2 + b**2 == c**2) and (a + b + c == p):
                solutions += 1
    return solutions

max_solutions = 0
max_p = 0
for p in range(1, 1001):
    solutions = find_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p

print(max_p)
p_max_solutions = 0
max_solutions = 0
for p in range(1, 1001):
    solutions = num_solutions(p)
    if solutions > max_solutions:
        p_max_solutions = p
        max_solutions = solutions
print(p_max_solutions)
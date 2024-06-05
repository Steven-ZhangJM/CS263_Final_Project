max_count = 0
max_perimeter = 0
for p in range(1, 1001):
    solutions = right_triangle_solutions(p)
    if solutions > max_count:
        max_count = solutions
        max_perimeter = p

print(max_perimeter)
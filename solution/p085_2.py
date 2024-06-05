import math

def count_rectangles(grid_size):
    total = 0
    for i in range(1, grid_size[0]+1):
        for j in range(1, grid_size[1]+1):
            total += (grid_size[0] - i + 1) * (grid_size[1] - j + 1)
    return total

def find_nearest_solution():
    grid_sizes = [(x, y) for x in range(2, 100) for y in range(2, 100)]
    nearest_grid = None
    min_diff = float('inf')
    for grid_size in grid_sizes:
        count = count_rectangles(grid_size)
        diff = abs(count - 2000000)
        if diff < min_diff:
            min_diff = diff
            nearest_grid = grid_size
    return (nearest_grid[0] * nearest_grid[1], min_diff)

print(find_nearest_solution())
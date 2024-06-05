def diagonal_sum(n):
    sum = 1
    for i in range(3, n+1, 2):
        sum += 4*i**2 - 6*(i-1)
    return sum

# Size of the grid
grid_size = 1001
print(diagonal_sum(grid_size))
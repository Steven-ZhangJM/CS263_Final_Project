import math

# Function to calculate number of routes in a grid
def calculate_routes(n, k):
    return math.comb(n + k, n)

# Grid size
grid_size = 20

# Calculate the number of routes for a 20x20 grid
routes = calculate_routes(grid_size, grid_size)
print(routes)
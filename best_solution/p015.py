import math

def count_routes(grid_size):
    routes = math.factorial(2*grid_size) // (math.factorial(grid_size)**2)
    return routes

grid_size = 20
print(count_routes(grid_size))
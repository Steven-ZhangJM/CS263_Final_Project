import math

def count_routes(n):
    return math.factorial(2*n) // (math.factorial(n)**2)

n = 20
routes = count_routes(n)
print(routes)
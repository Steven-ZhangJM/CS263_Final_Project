

import math

grid = 20*20 # the size of the grid
s = 2 # the stride of the grid.

res = math.factorial(grid) / (math.factorial(s-1) * math.factorial(grid-s))

print(int(res))
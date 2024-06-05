
import math
solved = None

for x in range(1, 200):
    for y in range(x, 200):
        z = math.sqrt(x**2 + y**2)
        if x + y + z == x == y == z:
            if z - x > 0 and z - y > 0 and x + z > y + z and x - z > y - z:
                solved = x, y, z
    if solved:
        break

print(solved)

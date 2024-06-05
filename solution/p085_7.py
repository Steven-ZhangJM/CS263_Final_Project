e Python code to solve the problem:

```
import math

def count_rectangles(grid_size):
    total = 0
    for i in range(1, grid_size[0] + 1):
        total += (grid_size[1] * i) // 2
    return total

low = 1
high = 2000000
found = False
while not found:
    mid = math.ceil((low + high) / 2.0)
    rectangles = count_rectangles(tuple([mid, 2]))
    if abs(2000000 - rectangles) < 1000: # we can't get exactly to 2 million, so 1000 is a reasonable tolerance
        found = True
        area = mid * 2
    elif rectangles > 2000000:
        high = mid - 1
    else:
        low = mid + 1

print(area)
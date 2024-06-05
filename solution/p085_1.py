```Python
import math

def count_rectangles(width, height):
    return width * height

min_diff = float('inf')
best_area = 0

for width in range(1, 100):  # Start from 1 and go up to 99
    for height in range(1, width+1):  # For each width, try all possible heights
        num_rectangles = count_rectangles(width, height)
        diff = abs(num_rectangles - 2000000)  # Calculate the difference between actual and desired number of rectangles

        if diff < min_diff:
            min_diff = diff
            best_area = width * height

print("The area of the grid with the nearest solution is", best_area)
```
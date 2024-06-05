e Python code to solve the problem:

```
import math

# Define the radii of the balls in mm
radii = [30, 31, 32, ..., 50]

# Initialize the length of the shortest pipe as infinity
length = float('inf')

# Iterate over all possible lengths of the pipe
for i in range(1, 100):  # Assuming the maximum radius is 50mm and the minimum radius is 30mm
    can_contain_all_balls = True
    for r in radii:
        if math.sqrt((2 * i) ** 2 + (r - 25) ** 2) > 50:  # Check if the ball can be contained by the pipe of length i
            can_contain_all_balls = False
            break
    if can_contain_all_balls:
        length = i
        break

# Convert the length to micrometres and round it to the nearest integer
length_in_um = int(round(length * 1000))

print(f"The length of the shortest pipe is {length_in_um} um.")
```
*
```python
import math

# Define the radii of the balls in mm
ball_radii = [30, 31, 32, ..., 50]

# Convert the radii from mm to micrometers (μm)
ball_radii_micro = [radius * 1000 for radius in ball_radii]

# Calculate the diameter of each ball in μm
ball_diameters_micro = [2 * radius for radius in ball_radii_micro]

# Define the internal radius of the pipe in mm
pipe_internal_radius_mm = 50

# Convert the internal radius from mm to micrometers (μm)
pipe_internal_radius_micro = pipe_internal_radius_mm * 1000

# Calculate the length of the shortest pipe that can fully contain all balls
pipe_length_micro = max(ball_diameters_micro) + 2 * pipe_internal_radius_micro

print(int(round(pipe_length_micro)))
```
**
```
import math

# Given values
inner_radius = 0.05  # in meters (50 mm)
radii = [0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 
         0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 
         0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 
         0.27, 0.28, 0.29, 0.30, 0.31, 0.32, 0.33, 0.34, 
         0.35, 0.36, 0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 
         0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.50]
outer_radius = max(radii)

# Calculate the length of the pipe
length = (2 * math.pi) * (inner_radius + outer_radius)
print(int(round(length * 10**6)))  # convert to micrometers and round to nearest integer
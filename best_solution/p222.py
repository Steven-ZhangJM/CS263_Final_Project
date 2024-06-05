import math

# Define the radii of the balls in mm
radii = [30, 31, 32, ..., 50]  # list comprehension to generate all numbers from 30 to 50

# Convert the radii from mm to um (1 mm = 1000 um)
radii_um = [r * 1000 for r in radii]

# Calculate the total volume of the balls
total_volume = sum(4/3 * math.pi * (r ** 3) for r in radii_um)

# Calculate the internal radius of the pipe in um
internal_radius_um = 50 * 1000

# Calculate the length of the shortest pipe that can fully contain the balls
length_um = (total_volume / math.pi) ** (1/3) + 2 * internal_radius_um

# Round the result to the nearest integer
result = round(length_um)

print(result)
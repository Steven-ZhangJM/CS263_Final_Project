import math

def calculate_length():
    internal_radius = 50e-3  # in meters
    outer_radii = [30, 31, 32, ..., 50]  # in millimeters
    
    length = 0
    for radius in outer_radii:
        length += (radius - internal_radius) + ((2 * math.pi * radius) - (2 * math.pi * internal_radius))
    
    return round(length / 10**-6)

print(calculate_length())

#
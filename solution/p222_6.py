import math

r = 50  # internal radius of pipe in mm
R = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]  # radii of balls in mm
d = [r - x for x in R]  # diameter of each ball

max_diameter = max(d)  # maximum diameter of a ball that can fit inside the pipe
shortest_pipe_length = 2 * math.pi * r + 2 * max_diameter

print(int(shortest_pipe_length * 1000))  # convert to micrometres and round to nearest integer

#
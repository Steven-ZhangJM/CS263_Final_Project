# Python code to solve the robot arc problem

from itertools import product

def is_valid_path(path):
    # Starting direction is north (0: north, 1: east, 2: south, 3: west)
    direction = 0
    for move in path:
        if move == 'C':
            # Clockwise move
            direction = (direction - 1) % 4
        else:
            # Anticlockwise move
            direction = (direction + 1) % 4
    # Check if the robot returns to the starting direction (north)
    return direction == 0

def count_valid_paths(arc_length):
    # Generate all possible combinations of 'C' (clockwise) and 'A' (anticlockwise) moves
    all_paths = product('CA', repeat=arc_length)
    # Filter valid paths that return to the starting position
    valid_paths = filter(is_valid_path, all_paths)
    return len(list(valid_paths))

# Calculate the number of valid paths for 70 arcs
number_of_paths = count_valid_paths(70)
print(number_of_paths)
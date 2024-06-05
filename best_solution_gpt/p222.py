# Python code to calculate the length of the shortest pipe in micrometres

# Function to calculate the total length required
def calculate_length(balls_radii, pipe_radius):
    total_length = 0
    for radius in balls_radii:
        total_length += 2 * (pipe_radius - radius)
    return total_length

# Given data
balls_radii = [i for i in range(30, 51)]  # Radii from 30mm to 50mm
pipe_radius = 50  # Pipe internal radius in mm

# Calculate the length in mm and convert to micrometres
length_mm = calculate_length(balls_radii, pipe_radius)
length_micrometres = length_mm * 1000  # Convert mm to micrometres

# Round to the nearest integer
length_micrometres_rounded = round(length_micrometres)

# Output the result
print(length_micrometres_rounded)
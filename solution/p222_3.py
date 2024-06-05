import math

def calculate_pipe_length():
    # Define the internal radius of the pipe in mm
    internal_radius_mm = 50
    
    # Calculate the maximum possible radius of a ball that can be contained within the pipe
    max_ball_radius_mm = internal_radius_mm
    
    # Initialize an empty list to store the radii of all balls that can be contained within the pipe
    ball_radii_mm = []
    
    for i in range(21):
        if 2 * (i + 1) > max_ball_radius_mm:
            break
        ball_radii_mm.append(i + 31)
    
    # Calculate the total diameter of all balls that can be contained within the pipe
    total_diameter_mm = sum(ball_radii_mm) * 2
    
    # Calculate the length of the shortest pipe required to contain all the balls
    pipe_length_mm = internal_radius_mm * math.pi + (total_diameter_mm / 2)
    
    # Convert the length from mm to micrometers
    pipe_length_um = pipe_length_mm * 1000
    
    return round(pipe_length_um)

# Calculate and print the result
print(calculate_pipe_length())

#
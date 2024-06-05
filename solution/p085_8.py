import math

def count_rectangles(width, height):
    return width * height * (width + 1) * (height + 1) // 2

def find_nearest_solution():
    nearest = None
    nearest_diff = float('inf')
    
    for width in range(1, 10000):  # we don't need to check up to 2 million, as the area will be too large
        height = math.ceil(2000000 / (width * (width + 1)) ** 0.5)
        
        rectangles = count_rectangles(width, height)
        diff = abs(rectangles - 2000000)
        
        if diff < nearest_diff:
            nearest = width
            nearest_diff = diff
            
    return width * height

print(find_nearest_solution())
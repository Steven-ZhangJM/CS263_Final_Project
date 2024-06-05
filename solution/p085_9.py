def count_rectangles(width, height):
    total = 0
    for i in range(1, width + 1):
        total += (width - i + 1) * height
    return total

def find_nearest_solution():
    min_diff = float('inf')
    nearest_width = 0
    nearest_height = 0
    for w in range(1, 100): # Try up to width 100
        for h in range(w, 101): # The height must be greater than or equal to the width
            count = count_rectangles(w, h)
            diff = abs(count - 2000000)  # The target is 2 million rectangles
            if diff < min_diff:
                min_diff = diff
                nearest_width = w
                nearest_height = h
    return nearest_width * nearest_height

print(find_nearest_solution())
#
def count_rectangles(w, h):
    return (w * (w + 1) * h * (h + 1)) // 4

def find_nearest_area(target):
    min_diff = float('inf')
    nearest_area = 0
    for w in range(1, 100):
        for h in range(1, 100):
            rect_count = count_rectangles(w, h)
            diff = abs(rect_count - target)
            if diff < min_diff:
                min_diff = diff
                nearest_area = w * h
    return nearest_area

# Find the area of the grid with the nearest solution to two million rectangles
area = find_nearest_area(2000000)
print(area)
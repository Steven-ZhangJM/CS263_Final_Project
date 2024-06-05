def count_rectangles(width, height):
    total = 0
    for w in range(1, width + 1):
        total += height
        for h in range(1, height + 1):
            if w * h > width * height: break
            total += 1
    return total

def find_nearest_solution(max_area):
    min_diff = float('inf')
    best_width = 0
    best_height = 0
    for w in range(1, int(max_area ** 0.5) + 1):
        for h in range(w, int(max_area / w) + 1):
            area = w * h
            diff = abs(area - max_area)
            if diff < min_diff:
                min_diff = diff
                best_width = w
                best_height = h
    return best_width * best_height

max_area = 2000000
best_area = find_nearest_solution(max_area)

print("The area of the grid with the nearest solution is:", best_area)
#
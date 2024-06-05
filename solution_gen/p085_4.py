


def rectangular_grid_num_of_rectangles_in_area_containing_30000(grid):
    num_of_rectangles = 0
    for row in range(len(grid) - 1):
        for col in range(len(grid[0]) - 1):
            area = (grid[row][col] + grid[row + 1][col]) * (grid[row][col + 1] + grid[row + 1][col + 1])
            height = grid[row][col] + grid[row + 1]
            width = grid[col][col] + grid[col][col + 1]
            if (area == 30000):
                num_of_rectangles += 1
                break
            elif (area > 30000):
                break
    
    return num_of_rectangles


print(rectangular_grid_num_of_rectangles_in_area_containing_30000([
    [5, 5, 5, 5],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 2, 2, 2]
]))


import unittest

def numRoutes(y, x, grid):
    movs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    moves = 0
    for x_mov, y_mov in movs:
        col = x
        row = y
        while 0 <= col < 20 and 0 <= row < 20:
            if grid[row][col] == "S":
                break
            row += y_mov
            col += x_mov
            moves += 1
    return moves

class Test(unittest.TestCase):
    '''Test Cases for the problem'''
    data = [
        (4, 6, '..#..',
        ['..#.': 3, '...#': 3, '..##.': 3, '.#..#.': 24, '.###.': 5, '.#.#.': 14])
    ]
    for y, x, grid, expected_result in data:
        result = numRoutes(y, x, grid)
        assert result == expected_result

if __name__ == "__main__":
    unittest.main()
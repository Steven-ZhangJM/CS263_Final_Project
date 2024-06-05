
from math import sqrt
from sys import maxsize


def solution():
    count = 0
    area = 0

    for x in range(1, 1000):
        for y in range(1, 1000):
            grid = x * y
            possible_num = sqrt(grid)
            if possible_num.is_integer() and grid <= 2000000:
                count += 1
                area = max(area, grid)
    return area


if __name__ == "__main__":
    if __name__ == "__main__":
        results = solution()
        print(results)

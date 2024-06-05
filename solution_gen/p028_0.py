

# import math
from math import floor, sqrt

n = int(input())
squares = []


def square_number(x):
    return x ** 2


def squares_from_square():
    result_sum = 0
    max_square = 0
    maxx, maxy, xc, yc = 0, 0, 0, 0
    for x in range_squares(squares, max_square):
        max_square = max(max_square, x)
        for y in range_squares(n - max_square - 1, max_square - 1, floor):
            result = square_number(x) + square_number(y)
            result_sum += result
            xc, yc = x, y

    return result_sum


def range_squares(squares, max_square):
    return range(0, max_square + 1) if squares else iter(range(1, max_square + 2, 2))


squares.extend(range(1, n + 1))
print(squares_from_square())

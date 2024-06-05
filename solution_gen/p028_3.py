

from math import sqrt

R = 5


def spiral(wsize, rsize):
    def spiral_row(row, col):
        top, bot = row - rsize, row + rsize
        left, rigt = col - wsize, col + wsize
        return [row, left, top, rigt]

    result = [spiral_row(row, col) for row in range(rsize) for col in range(wsize)]
    return map(lambda p: sum(p), map(lambda x: str(x).split(' '), map(lambda coords: str(coords).replace(',', ''),
                                                                              ''.join(sorted([str(x) for x in result])))))


print(spiral(R, R))

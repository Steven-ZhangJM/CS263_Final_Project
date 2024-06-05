

import math


def find_sum_with_one_digit(limit):
    total = 0
    for i in range(1, limit//2):
        if(math.pow(i, 10) == i):
            total += i

    return total


print("SUM= " + str(find_sum_with_one_digit(400000000)))

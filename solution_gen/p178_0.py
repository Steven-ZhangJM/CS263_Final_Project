

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = 5000
    sys.setrecursionlimit(
        int(math.ceil((math.sqrt(1 + 8 * n) - 1) / 2)))

    # Determine how many integers are less than or equal to 10^40
    all_integers = range(10 ** 37 + 1)
    p = 0
    for i in all_integers:
        if i < 10 ** 40:
            is_pandigital = True
            num = str(i)
            for digit in num:
                if digit not in '3456789':
                    is_pandigital = False
                    break
                else:
                    continue
            if is_pandigital:
                p += 1
    print(p + 2)



from itertools import product

def solution1(start, end, max_digit = 4):
    arr = []
    for i in product(range(10), repeat = max_digit):
        for n in product(range(10), repeat = max_digit):
            if len(str(int("".join(i)) * int("".join(n)))) == max_digit:
                for m in product(range(10), repeat = max_digit):
                    if "".join(m) == "-".join(int("".join(n))):
                        arr = arr + [int("".join(n))]
    return max(arr)


print(solution1(100, 999))

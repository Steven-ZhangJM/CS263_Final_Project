
# import math
# import time


def num(i):
    return list(map(int, str(i)))


def solve():
    # start_time = time.time()
    solution = 0
    i = 0
    while True:
        temp = list(num(i))
        if sum(temp) > 90:
            break
        elif sum(temp) < 10:
            solution += 1
        i += 1
    return solution


# print("%0.3fs" % (time.time() - start_time))  # take a break
print(solve())

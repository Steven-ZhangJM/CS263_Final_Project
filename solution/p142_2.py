import math

def find_smallest_x():
    smallest_sum = float('inf')
    for x in range(1, int(math.sqrt(smallest_sum)) + 1):
        for y in range(x - 1, 0, -1):
            z = x - y
            if (x + y) ** 2 == ((x + y) ** 2) % 4 and \
               (x - y) ** 2 == ((x - y) ** 2) % 4 and \
               (x + z) ** 2 == ((x + z) ** 2) % 4 and \
               (x - z) ** 2 == ((x - z) ** 2) % 4 and \
               (y + z) ** 2 == ((y + z) ** 2) % 4 and \
               (y - z) ** 2 == ((y - z) ** 2) % 4:
                return x + y + z
    return smallest_sum

print(find_smallest_x())

#
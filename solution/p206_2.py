import math

def find_square():
    for i in range(1, 10**6):
        square = str(i ** 2)
        if len(square) == 9 and set('0123456789') == set(square[0]):
            return i

print(find_square())
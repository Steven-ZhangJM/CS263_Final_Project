import itertools

def find_square():
    for i in range(1, 100):
        square = str(i ** 2)
        if len(square) == 10 and '0' in square[4:] and set('123456789') == set(square[:4]):
            return i

print(find_square())
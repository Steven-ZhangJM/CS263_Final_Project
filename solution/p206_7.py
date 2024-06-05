def find_positive_integer():
    for i in range(1, 100):
        square = str(i ** 2)
        if len(square) == 10 and set('0123456789') == set(square[0]):
            return i

print(find_positive_integer())
#
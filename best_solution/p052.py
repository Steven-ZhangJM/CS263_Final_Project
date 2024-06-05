def find_x():
    for x in range(1, 1000000):  # try up to 10^6
        digits = set(str(x))  # get unique digits of x
        if all(set(str(i*x)) == digits for i in [2, 3, 4, 5, 6]):
            return x

print(find_x())
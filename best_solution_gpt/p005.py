def smallest_multiple(n):
    if n <= 2:
        return n
    multiple = n
    while True:
        for i in range(n, 1, -1):
            if multiple % i != 0:
                break
        else:
            return multiple
        multiple += n

# Smallest multiple for numbers 1 to 20
print(smallest_multiple(20))
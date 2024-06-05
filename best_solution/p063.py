n = 5  # start with 5 digits
print(find_powers(n))

n = 9   # then 9 digits
print(find_powers(n))

n = 10  # maximum possible number of digits (for now)
while True:
    print(find_powers(n))
    n += 1
    if find_powers(n) == 0:
        break
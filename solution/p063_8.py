def find_n_digit_powers():
    count = 0
    for n in range(1, 10):
        for i in range(2, 100000):  # arbitrarily set an upper limit
            if len(str(i**n)) == n:
                count += 1
    return count

print(find_n_digit_powers())

#
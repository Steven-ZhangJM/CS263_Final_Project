


def last_digit(x):
    return sum(
        x**i // 10 for i in range(0, x.bit_length() - 10) + list(range(10, 100000))
    ) % 10000


print(last_digit(100))


"""





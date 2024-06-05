


def fib(n):
    if n < 3:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, b + a
    return b


if __name__ == '__main__':
    print(fib(1001))



from math import prod


def get_answer():
    return prod(
            int(x / 5) for x in pis(int((1_000_000_000_000)))
    )


def pis(n):
    return [str(n), str(n)[:5]]


if __name__ == '__main__':
    print(get_answer())

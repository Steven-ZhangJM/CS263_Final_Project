
from lib.n_digit_numbers import n_digit_numbers


def count_n_bigger_than(n: int) -> int:
    """
    >>> count_n_bigger_than(987654321)
    2
    >>> count_n_bigger_than(12345)
    1
    >>> count_n_bigger_than(0)
    0
    """
    i = 0
    for i in range(1, 10 ** n):
        if n_digit_numbers(i) >= 2:
            return i

    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

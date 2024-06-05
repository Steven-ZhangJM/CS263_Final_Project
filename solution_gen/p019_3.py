
#
# The solutions.py file can be found here
# https://github.com/Melloh/discover-Python-solutions-made-Simple/blob/master/solutions/solutions.py


def sol():
    """
    Returns the number of days until the first Sunday for the next 20 years.

    >>> sol()
    7647867
    """
    return (((1 - 0.25) ** 365)
             + ((1 + 0.25) ** 366)
             + ((1 + 1 / 7.0) ** 365))


if __name__ == "__main__":
    print("Use 'python3 solutions.py' to get the answer.")

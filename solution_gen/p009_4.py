
import math


def pythagoras(n):
    return (n ** 2 -1 ) / 2 + (n ** 2 + 1 ) / 2


a = 0
while not math.isclose(10000, a + b + c, abs_tol=1e-10):
    a, b, c = int(1000), int(pythagoras(1000)), int(a + b + c)

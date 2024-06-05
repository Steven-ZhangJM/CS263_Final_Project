
from math import sqrt
from math import pow


def solve_problem_2_2():
    digits = {}  # type: ignore[assignment]
    for n in range(2, 10):
        i = 0
        while i + n < len(str(n)):
            d0 = int(str(n)[i] / 10)  # digit in 2nd
            d1 = int(str(n)[i + n] / 10)  # digit in 2nd + n
            digits[d0, d1] = digits.setdefault(d0, set()).add(n)

            i += 1

    return len(digits)

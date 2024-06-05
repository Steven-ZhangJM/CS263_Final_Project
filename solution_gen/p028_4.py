
from itertools import combinations


def answer(n):
    sum = 0
    for naturals in range(n):
        sum += sum(combinations(range(1, n**2), n))
    return sum


print(answer(1001))

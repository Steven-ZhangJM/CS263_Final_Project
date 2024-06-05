
from itertools import product
from collections import defaultdict

from utils import timeit


@timeit
def get_answer():
    possible_solutions = defaultdict(int)
    for p in range(1, 1000):
        if p == 120:
            continue
        perimeter_triangle = 0
        for n in range(3):
            perimeter_triangle += n * (n + 1) >> 1
        solutions = 0
        if perimeter_triangle > p:
            solutions = (p - 1) / 2 + 1
            solutions -= solutions * perimeter_triangle // 120
        possible_solutions[perimeter_triangle] += solutions
    return max(possible_solutions, key=lambda x: possible_solutions[x])


if __name__ == "__main__":
    print(f"The answer is {get_answer()}")

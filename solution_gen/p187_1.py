

import util


def find_all_factors(target: int) -> list:
    factors = []
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            factors.append(i)
            factors.append(target // i)
    return set(factors)


def is_prime_two(n: int) -> bool:
    if n >= 2 and n <= 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def get_total() -> int:
    target = 1
    while True:
        temp = find_all_factors(target)
        if len(temp) == 2 and is_prime_two(min(temp) ** 2):
            return target
        target += 1


util.calc_stat(get_total, 'comp
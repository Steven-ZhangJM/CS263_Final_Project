
from math import sqrt

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x % 2 == 0:
        return False
    i = 3
    sq_root = int(sqrt(x))
    while i <= sq_root:
        if x % i == 0:
            return False
        i += 2
    return True

def count_consec_primes(lowest_target: int, consecutive_number_sum: int):
    """
    Counts how many numbers that would lead to consecutive primes smaller than 'lowest_target'.
    """
    sum_of_all_consec_prime_numbers = consecutive_number_sum
    while int(sqrt(sum_of_all_consec_prime_numbers)) ** 2 == consecutive_number_sum:
        if is_prime(sum_of_all_consec_prime_numbers):
            consecutive_number_sum += 1
        sum_of_all_consec_prime_numbers += 1
    return consecutive_number_sum
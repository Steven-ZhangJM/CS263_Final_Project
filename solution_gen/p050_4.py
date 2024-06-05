
from typing import List
from math import sqrt


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_test(number: int) -> int:
    if is_prime(number):
        return number
    else:
        return False


def prime_series_of_sum(number: int) -> int:
    number_list = (5, 3, 7, 11, 13, 17, 19, 23, 29)
    largest_contig_sum = 0
    largest_contig_end = 0
    prime = is_prime_test(number)
    while prime <= number:
        prime_number = is_prime_test(prime)
        largest_contig_sum += prime_number
        largest_contig_end += number_list[number_list.index(prime_number)]
        if largest_contig_sum == largest_contig_end:
            return largest_contig_sum
        prime = prime + number_list[number_list.index(prime_number)]


if __name__ == '__main__':
    print(prime_series_of_sum(1000))

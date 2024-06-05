
from math import sqrt
from itertools import permutations
from functools import reduce

def is_palindromic(n):
    s = str(n)
    return s == s[::-1]

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for d in range(5, int(sqrt(n)) + 1, 6):
        if n % d == 0 or n % (d - 2) == 0:
            return False
    return True


def is_prime_right(n):
    if n % 2 == 0 or n % 3 == 0:
        if n == 2:
            return True
        if n == 3:
            if n == 5:
                return True
        else:
            return False
    r = n % 10
    for d in range(5, r, 6):
        if n % d == 0 or n % (d - 2) == 0:
            return False
    return True


def make_divisors(n):
    small_divisors, large_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small_divisors.append(i)
            if i!= n // i:
                large_divisors.append(n//i)
        i += 1
    return small_divisors + large_divisors[::-1]


def is_right_truncatable(n):
    if is_palindromic(n):
        return True
    divisors = make_divisors(n)
    for d in divisors:
        if not is_prime(d) or not is_prime_right(n // d):
            return False
    return True


def prime_with_2_digit_sum(s):
    digits = set(str(i) for i in range(10))
    for num in str(s):
        if num in digits:
            digits.discard(num)
        else:
            digits.add(num)
    possible_palindromic = range(10, 100)
    for p in possible_palindromic:
        prime_number = str(p)
        for i in range(3):
            prime_number = prime_number[p:] + prime_number[:p]
            if prime_number == prime_number[::-1]:
                if is_palindromic(prime_number):
                    if not digits.intersection(prime_number) and is_prime_right(int(prime_number)):
                        return prime_number
    return False


def sum_primes():
    primes = list(filter(is_prime, range(1, 1_000_000)))
    for s in primes:
        r = list(map(int, str(s)))
        if all(is_right_truncatable(n) for n in permutations(r)):
            prime = prime_with_2_digit_sum(s)
            if prime:
                return sum(primes) - s
    return False


if __name__ == '__main__':
    print(sum_primes())

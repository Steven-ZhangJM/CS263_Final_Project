

import math

def largest_pandigital_prime():
    def find_prime_digits(n):
        return len(set([i for i in range(1, n + 1) if math.sqrt(i ** 2) - i == 0])) == 1

    return str(int(''.join(filter(str.isdigit, str(2 ** (largest_digit() + 1)))))),

# print(largest_pandigital_prime())

def largest_pandigital_prime_1():
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        else:
            n += 1
            sqrt = int(sqrt)
            for divisor in range(sqrt, int(math.sqrt(n)) + 2):
                if n % divisor == 0 or n % (divisor + 2) == 0:
                    return False
            return True

    n = 1
    while True:
        candidate, number = n, int(str(n) * len(str(n)))
        if not is_prime(number):
            return candidate
        n += 1


def largest_pandigital_prime_2():
    def p_digits(n):
        digits = str(int(''.join(filter(str.isdigit, str(n))))).zfill(len(str(n)))
        max_value = int(''.join(filter(str.isdigit, str(n))))
        min_value = int(''.join(filter(str.isdigit, str(n)))) - 1
        number = False
        for d, dv in items(range(max_value, min_value, -1)):
            if d < min_value or d > max_value:
                break
            if not any(int(d) in digits[i] for i in range(len(digits))):
                number = True
        return number

    n = 1
    while True:
        candidate = n
        if p_digits(candidate):
            return candidate
        n += 1

max_prime = largest_pandigital_prime_2()
print(max_prime)



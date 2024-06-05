from math import sqrt

def is_perfect_square(n):
    return int(sqrt(n)) ** 2 == n

def sigma_2(n):
    total = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            total += i**2
            if i != n // i:
                total += (n // i)**2
    return total

def compute():
    LIMIT = 64000000
    result = 0
    for i in range(1, LIMIT):
        if is_perfect_square(sigma_2(i)):
            result += i
    return result

print(compute())
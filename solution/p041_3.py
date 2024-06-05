import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_pandigitals(n):
    pandigitals = []
    for i in range(10**n-1, 9, -1):  # start from largest possible number
        digits = [int(d) for d in str(i)]
        if len(set(digits)) == n and max(digits) <= n:  # check if pandigital
            pandigitals.append(i)
    return pandigitals

def find_largest_pandigital_prime(n):
    pandigitals = generate_pandigitals(n)
    largest_prime = None
    for p in pandigitals:
        if is_prime(p) and (largest_prime is None or p > largest_prime):
            largest_prime = p
    return largest_prime

n = 6  # start from 6-digit numbers, since the problem statement implies this
while True:
    result = find_largest_pandigital_prime(n)
    if result is not None:
        print(result)
        break
    n += 1
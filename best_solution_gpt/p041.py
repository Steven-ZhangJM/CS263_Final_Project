from itertools import permutations
from sympy import isprime

def largest_pandigital_prime():
    # Start with the largest n-digit pandigital number and go down
    for n in range(9, 0, -1):
        pandigitals = permutations('123456789'[:n])
        for p in sorted(pandigitals, reverse=True):
            num = int(''.join(p))
            if isprime(num):
                return num
    return None

# Call the function and print the result
print(largest_pandigital_prime())
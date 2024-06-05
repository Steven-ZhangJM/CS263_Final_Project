from sympy import isprime

def rotate_number(n):
    return [int(str(n)[i:] + str(n)[:i]) for i in range(len(str(n)))]

def is_circular_prime(n):
    return all(isprime(num) for num in rotate_number(n))

circular_primes = [n for n in range(2, 1000000) if is_circular_prime(n)]
print(len(circular_primes))
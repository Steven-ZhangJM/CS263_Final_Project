


import math
import time
start = time.time()
def is_prime(n):
    if not n % 2:
        return False
    k = int(math.sqrt(n) + 1)
    for _ in range(3, k, 2):
        if n % _ == 0:
            return False
    else:
        return True

def pandigital_prime(n):
    pandigital = str(string_to_nint(n))
    n_digits_to_consider = math.floor(math.log10(n)) + 1
    d_set = set()
    for digit in range(n_digits_to_consider):
        d_set.add(digit)
    prime = False
    for d in d_set:
        if pandigital[d] == 0:
            if not is_prime(int(pandigital)):
                prime = True
                break
    if prime:
        return pandigital

all_primes = []
for prime in range(2, 10001):
    if is_prime(prime):
        all_primes.append(prime)
        for i in range(2,prime+1):
            
            # prime % 2!=0
            if prime % i!= 0:
                print(prime,i)
                print(prime * i)
            if i == prime:
                print(prime,i,'i is equal to',prime)

candidate = min(all_primes, key=lambda x: (pandigital_prime(x).count(str(None)), len(pandigital_prime(x))))
print(is_prime(candidate), 'primes are found')
print(candidate)
print(pandigital_prime(candidate))

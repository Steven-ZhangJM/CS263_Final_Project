ython program to find the maximum $n$-digit pandigital prime:

```Python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_pandigital(n):
    digits = str(n)
    return set(str(n)) == set('123456789'[:len(digits)])

max_prime = 0

for n in range(9, 0, -1):  # Start from 9 and go down to 2
    for i in range(10**(n-1), 10**n):
        if is_pandigital(i) and is_prime(i):
            max_prime = i
            break

print("The maximum {}-digit pandigital prime that exists is {}".format(len(str(max_prime)), max_prime))
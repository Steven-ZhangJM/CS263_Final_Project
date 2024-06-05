def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for n in range(2, 10**8):  # iterate over all numbers less than 10^8
    factors = set()
    for p in range(2, int(n**0.5) + 1):
        while n % p == 0:
            factors.add(p)
            n //= p
    if n > 1:  # if n is still a prime number
        factors.add(n)
    if len(factors) == 2:  # if there are precisely two factors (prime or not)
        count += 1

print(count)  # print the result
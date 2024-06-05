import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_sum_of_primes(n):
    primes = []
    sum_count = 0
    for p in range(2, n + 1):
        if is_prime(p):
            primes.append(p)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            total = sum(primes[i:j+1])
            if total > n:
                break
            if total == n:
                sum_count += 1
    return sum_count

start = 2
while True:
    count = count_sum_of_primes(start)
    if count > 5000:
        print(f"The first value which can be written as the sum of primes in over five thousand different ways is {start}.")
        break
    start += 1

#
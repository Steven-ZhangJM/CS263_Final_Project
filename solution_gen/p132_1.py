

# Solution

import time

startTime = time.time()

def find(number):
    count = 1
    factors = []
    for i in range(1, round(number ** 0.5) + 1):
        if number % i == 0:
            count += 1
            factors.append(i)
            factor_2 = number / i
            while factor_2 % i == 0:
                count += 1
                factor_2 /= i
        if count > 4:
            break

    return factors, count


prime_numbers = []
factors = []
num = 1

while sum(factors) < 4000000:
    prime, factor = find(num)
    prime_numbers += prime
    factors.append(factor)
    num += 1


print(10 ** 9, (sum([i * j for i, j in enumerate(prime_numbers)])))

print(time.time() - startTime)

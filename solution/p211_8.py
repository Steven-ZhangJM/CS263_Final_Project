import math

def sigma2(n):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i ** 2
            if i != n // i and n // i <= int(math.sqrt(n)):
                sum += (n // i) ** 2
    return sum

count = 0
total_sum = 0
for n in range(1, 64000000):
    sigma_value = sigma2(n)
    sqrt_sigma = math.isqrt(sigma_value)
    if sqrt_sigma * sqrt_sigma == sigma_value:
        count += 1
        total_sum += n

print(count, total_sum)
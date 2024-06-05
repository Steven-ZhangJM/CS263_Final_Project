def sum_of_squares(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0:
            result += i ** 2
    return result


squares_sum = 0
for n in range(1, 64000000):
    sigma_2_n = sum_of_squares(n)
    sqrt_sigma_2_n = int(sigma_2_n ** 0.5) + 1
    if sqrt_sigma_2_n * sqrt_sigma_2_n == sigma_2_n:
        squares_sum += n

print(squares_sum)

#
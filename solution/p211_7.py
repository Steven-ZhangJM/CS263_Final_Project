total_sum = 0
for n in range(1, 64000000):
    if is_perfect_square(sigma2(n)):
        total_sum += n
print(total_sum)
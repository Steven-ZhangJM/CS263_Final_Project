sum = 0
for n in range(1, 64000000 + 1): 
    if is_perfect_square(sigma_2(n)):
        sum += n
print(sum)
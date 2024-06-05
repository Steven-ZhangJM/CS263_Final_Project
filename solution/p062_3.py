min_cube = 1000000
for i in range(1, min_cube + 1):
    if i ** (1/3) % 1 == 0:
        if permute_digits(i) == 5:
            print(f"The smallest cube for which exactly five permutations of its digits are cube is: {i}")
            break
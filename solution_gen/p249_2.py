

S = 0
for i in range(-3,2):
    x = get_primes_between_1_and(5000-i)

    if not primes_list_1st_digits_prime(x):
        S = S + len(x)
        if len(x) > 16:
            break

print('sum of subsets ',S)

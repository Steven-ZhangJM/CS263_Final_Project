count = 0
for n in range(2, 10**7):
    if count_divisors(n) == count_divisors(n + 1):
        count += 1
print(count)
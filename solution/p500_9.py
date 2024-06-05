k = 1
while True:
    if count_divisors(k) == 2 ** 500500:
        print(k % 500500507)
        break
    k += 1

#
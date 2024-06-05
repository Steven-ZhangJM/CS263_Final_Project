a2 = 512
power = 3

while True:
    a10 = a2 ** power
    print(a10)
    if a10 == 614656:
        break
    a2, power = a10, power + 1

print(find_power_sum(a2))
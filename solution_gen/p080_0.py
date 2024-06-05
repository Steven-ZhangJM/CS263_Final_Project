

digit_sum = 0

for i in range(1, 101):
    x = int(str(int(i**.5))[:1000])
    digit_sum += x

print(digit_sum)


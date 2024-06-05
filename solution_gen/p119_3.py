

a2 = 512
n = 3

sum = 0
while n > 0:
    sum += a2
    a2 = int(str(a2)[1:])*int(str(a2)[0])
    n -= 1

print(sum)
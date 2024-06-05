

n = 999
total = 0

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        total += i
print(total)




from math import sqrt

# n^3 + n^2 + 2n + 8 = n^2
max_n = (2**31)-1
min_n = -(2**31)

n_pow_of_11 = set()

for i in range(min_n, max_n):
    if i**2 <= max_n <= (i + 1)**2 and (i + 2 <= max_n <= i**2-i+1):
        n_pow_of_11.add(i*11)

ans = 0
for i in range(min_n, max_n):
    # print(i)
    if i not in n_pow_of_11:
        # print(i-1)
        if 2 in {int(str(i-1)*3), int(str(i-1)[1:2]*3), int(str(i-1)[2:3]*3)}:
            # print(i - 1, int(str(i-1)[2:3]), int(str(i-1)[1
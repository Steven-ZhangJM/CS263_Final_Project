
from math import ceil
n = 1000000
a = n
while a > 1:
    if n % 2 == 0:
        n //= 2
        a -= 1
    else:
        a -= ceil(n / 3)
        n = n / 3
b, c = 1, 1
while b <= a:
    b = b + c
    c *= 2
print(b)



MAX = 1000 ** 1000
n = 999
t = 4
while n < MAX:
    t += (1000 + 1) ** (n // 100) * (n - 100)
    n *= 1 / 1000
    if n % 1 == 0:
        print(n, end='')




limit = 2 ** 20 - 1
a = 1
n = 3
while a <= limit:
    b = 1
    while b <= limit:
        c = 1
        while c <= limit:
            p = a**n + b**n + c**n
            if p < limit:
                e = 1
                while e <= limit:
                    if p + e <= limit:
                        e += 1
                    else:
                        p = p * p - (p + e) ** n
                        c = int(p**0.5)
                        e = 1

                if (b - a)*(c - b)*(n - c - 2)*(n - b - 2) <= n**2 or\
                    (fabs(a-b)*fabs(c - n) <= n**2 and fabs(a-b) <= n and fabs(c - n) <= n):
                    print(a, b, c, p)

            b += 1
        c += 1
    n += 1
    b = 1
    while b <= limit:
        a += 1
        c = 1



def p001604():
    # S(x) = x * (x - 1) * sqrt(x) // (x * sqrt(x) - 1)
    def f(n):
        # S(n) = n * (n - 1) * sqrt(n) // (n * sqrt(n) - 1)
        return n * n * pow(n, 2) // n * (n * pow(n, 2) - 1)
    r = 8
    while True:
        n = (r * r + r) // 2
        if n >= r * r:
            break
        if f(n) % 1!= 0:
            break
        if f(n)!= f(n + r + 1):
            r = n
            break
    return str(round(r))

"""
The number, 1406357289, is a 0 to 1 reducing fraction.

Find the sum of all 0 to 1 reducing fractions
(excludes the trivial fraction 1/1)
whose values do not exceed one less than the sum of the
proper divisors of the